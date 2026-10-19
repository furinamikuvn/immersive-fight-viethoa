import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

public class BatchPatchAllHotaiBadiffs {
    public static void main(String[] args) throws Exception {
        String baseDir = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa";
        String hotaiDir = baseDir + "/hotai";
        String modsDir = baseDir + "/mods";
        String dictPath = "D:/minecraft mod trung/tools/hotai_dict.json";

        System.out.println("=== TAWA BATCH HOTAI BADIFF VIETNAMESE PATCHER ===");

        // 1. Load dictionary
        System.out.println("Loading translation dictionary from " + dictPath + "...");
        Map<String, String> dict = new LinkedHashMap<>();
        try (InputStream is = Files.newInputStream(Paths.get(dictPath));
             BufferedReader reader = new BufferedReader(new InputStreamReader(is, "UTF-8"))) {
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            // Parse simple JSON map
            String json = sb.toString();
            Pattern p = Pattern.compile("\"((?:\\\\.|[^\"\\\\])*)\"\\s*:\\s*\"((?:\\\\.|[^\"\\\\])*)\"");
            Matcher m = p.matcher(json);
            while (m.find()) {
                String k = unescapeJson(m.group(1));
                String v = unescapeJson(m.group(2));
                if (!k.isEmpty() && !v.isEmpty() && !k.equals(v)) {
                    dict.put(k, v);
                }
            }
        }
        System.out.println("Loaded " + dict.size() + " active translation pairs.");

        // Sort dictionary keys by length descending to match longest phrases first
        List<Map.Entry<String, String>> sortedDict = new ArrayList<>(dict.entrySet());
        sortedDict.sort((a, b) -> Integer.compare(b.getKey().length(), a.getKey().length()));

        // 2. Index all classes in mods/
        System.out.println("Indexing jar classes in " + modsDir + "...");
        Map<String, Path> classToJar = new HashMap<>();
        try (DirectoryStream<Path> ds = Files.newDirectoryStream(Paths.get(modsDir), "*.jar")) {
            for (Path jarPath : ds) {
                try (ZipFile zf = new ZipFile(jarPath.toFile())) {
                    Enumeration<? extends ZipEntry> entries = zf.entries();
                    while (entries.hasMoreElements()) {
                        ZipEntry ze = entries.nextElement();
                        if (ze.getName().endsWith(".class")) {
                            classToJar.put(ze.getName(), jarPath);
                        }
                    }
                } catch (Exception e) {
                    // skip corrupted jars
                }
            }
        }
        System.out.println("Indexed " + classToJar.size() + " classes across all mod jars.");

        // 3. Scan all .badiff files in hotai/
        List<Path> badiffFiles = new ArrayList<>();
        Files.walkFileTree(Paths.get(hotaiDir), new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult visitFile(Path file, java.nio.file.attribute.BasicFileAttributes attrs) {
                if (file.toString().endsWith(".badiff")) {
                    badiffFiles.add(file);
                }
                return FileVisitResult.CONTINUE;
            }
        });
        System.out.println("Found " + badiffFiles.size() + " .badiff files in hotai/.");

        Pattern zhPattern = Pattern.compile("[\u4e00-\u9fff]");
        int patchedFilesCount = 0;
        int totalReplacedStrings = 0;
        int verifiedCount = 0;

        for (Path badiffPath : badiffFiles) {
            Path rel = Paths.get(hotaiDir).relativize(badiffPath);
            String relStr = rel.toString().replace('\\', '/');
            String clzName = relStr.substring(0, relStr.length() - ".badiff".length()) + ".class";

            Path jarPath = classToJar.get(clzName);
            if (jarPath == null) {
                continue;
            }

            // Read original class bytes
            byte[] origBytes = null;
            try (ZipFile zf = new ZipFile(jarPath.toFile())) {
                ZipEntry ze = zf.getEntry(clzName);
                if (ze != null) {
                    try (InputStream is = zf.getInputStream(ze)) {
                        origBytes = is.readAllBytes();
                    }
                }
            }
            if (origBytes == null) {
                continue;
            }

            // Apply existing diff
            MemoryDiff diff = new MemoryDiff();
            try (InputStream is = Files.newInputStream(badiffPath)) {
                diff.deserialize(DefaultSerialization.newInstance(), is);
            } catch (Exception e) {
                continue;
            }

            byte[] currentPatched;
            try {
                currentPatched = MemoryDiffs.apply(origBytes, diff);
            } catch (Exception e) {
                continue;
            }

            // Parse bytecode with ASM
            ClassReader cr = new ClassReader(currentPatched);
            ClassNode cn = new ClassNode();
            cr.accept(cn, 0);

            int fileReplaced = 0;
            for (MethodNode mn : cn.methods) {
                for (AbstractInsnNode insn : mn.instructions) {
                    if (insn instanceof LdcInsnNode ldc && ldc.cst instanceof String str) {
                        if (zhPattern.matcher(str).find()) {
                            String newStr = str;
                            for (Map.Entry<String, String> entry : sortedDict) {
                                if (newStr.contains(entry.getKey())) {
                                    newStr = newStr.replace(entry.getKey(), entry.getValue());
                                }
                            }
                            if (!newStr.equals(str)) {
                                ldc.cst = newStr;
                                fileReplaced++;
                                totalReplacedStrings++;
                            }
                        }
                    }
                }
            }

            if (fileReplaced > 0) {
                ClassWriter cw = new ClassWriter(0);
                cn.accept(cw);
                byte[] vietnamesePatched = cw.toByteArray();

                // Compute new diff
                MemoryDiff newDiff = MemoryDiffs.diff(origBytes, vietnamesePatched);

                // Backup and write
                Path backup = Paths.get(badiffPath.toString() + ".bak");
                if (!Files.exists(backup)) {
                    Files.copy(badiffPath, backup);
                }

                try (OutputStream os = Files.newOutputStream(badiffPath)) {
                    newDiff.serialize(DefaultSerialization.newInstance(), os);
                }

                // Verify
                MemoryDiff verifyDiff = new MemoryDiff();
                try (InputStream is = Files.newInputStream(badiffPath)) {
                    verifyDiff.deserialize(DefaultSerialization.newInstance(), is);
                }
                byte[] testApplied = MemoryDiffs.apply(origBytes, verifyDiff);
                if (Arrays.equals(testApplied, vietnamesePatched)) {
                    verifiedCount++;
                } else {
                    System.err.println("Verification warning for " + relStr);
                }

                patchedFilesCount++;
                System.out.println("Patched " + relStr + " (" + fileReplaced + " strings)");
            }
        }

        System.out.println("\n=== SUMMARY ===");
        System.out.println("Total badiff files patched with Vietnamese: " + patchedFilesCount);
        System.out.println("Total string constants translated: " + totalReplacedStrings);
        System.out.println("Total diffs verified successfully: " + verifiedCount);
    }

    private static String unescapeJson(String input) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < input.length()) {
            char c = input.charAt(i);
            if (c == '\\' && i + 1 < input.length()) {
                char next = input.charAt(i + 1);
                if (next == 'u' && i + 5 < input.length()) {
                    try {
                        int code = Integer.parseInt(input.substring(i + 2, i + 6), 16);
                        sb.append((char) code);
                        i += 6;
                        continue;
                    } catch (NumberFormatException e) {
                        // ignore
                    }
                } else if (next == 'n') { sb.append('\n'); i += 2; continue; }
                else if (next == 'r') { sb.append('\r'); i += 2; continue; }
                else if (next == 't') { sb.append('\t'); i += 2; continue; }
                else if (next == '"') { sb.append('"'); i += 2; continue; }
                else if (next == '\\') { sb.append('\\'); i += 2; continue; }
            }
            sb.append(c);
            i++;
        }
        return sb.toString();
    }
}
