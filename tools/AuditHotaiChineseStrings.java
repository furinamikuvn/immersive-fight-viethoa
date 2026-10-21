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

public class AuditHotaiChineseStrings {
    public static void main(String[] args) throws Exception {
        String hotaiDir = "D:/file tam mc/hotai";
        String modsDir = "D:/file tam mc/mods";

        System.out.println("Indexing classes in " + modsDir + "...");
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
                } catch (Exception e) {}
            }
        }
        System.out.println("Indexed " + classToJar.size() + " classes.");

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
        System.out.println("Found " + badiffFiles.size() + " badiff files.");

        Pattern zhPattern = Pattern.compile("[\u4e00-\u9fff]");
        int chineseFilesCount = 0;
        int totalChineseStrings = 0;

        for (Path badiffPath : badiffFiles) {
            Path rel = Paths.get(hotaiDir).relativize(badiffPath);
            String relStr = rel.toString().replace('\\', '/');
            String clzName = relStr.substring(0, relStr.length() - ".badiff".length()) + ".class";

            Path jarPath = classToJar.get(clzName);
            if (jarPath == null) {
                System.out.println("MISSING JAR FOR: " + relStr);
                continue;
            }

            byte[] origBytes = null;
            try (ZipFile zf = new ZipFile(jarPath.toFile())) {
                ZipEntry ze = zf.getEntry(clzName);
                if (ze != null) {
                    try (InputStream is = zf.getInputStream(ze)) {
                        origBytes = is.readAllBytes();
                    }
                }
            }
            if (origBytes == null) continue;

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

            ClassReader cr = new ClassReader(currentPatched);
            ClassNode cn = new ClassNode();
            cr.accept(cn, 0);

            List<String> found = new ArrayList<>();
            for (MethodNode mn : cn.methods) {
                for (AbstractInsnNode insn : mn.instructions) {
                    if (insn instanceof LdcInsnNode ldc && ldc.cst instanceof String str) {
                        if (zhPattern.matcher(str).find()) {
                            found.add("[" + mn.name + "] " + str);
                        }
                    }
                }
            }

            if (!found.isEmpty()) {
                chineseFilesCount++;
                totalChineseStrings += found.size();
                System.out.println("\n>>> FILE: " + relStr + " (" + found.size() + " strings):");
                for (String s : found) {
                    System.out.println("    " + s);
                }
            }
        }

        System.out.println("\n=== SUMMARY ===");
        System.out.println("Total files with Chinese: " + chineseFilesCount);
        System.out.println("Total Chinese strings: " + totalChineseStrings);
    }
}
