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

public class CheckAllAppliedClasses {
    public static void main(String[] args) throws Exception {
        String baseDir = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa";
        String hotaiDir = baseDir + "/hotai";
        String modsDir = baseDir + "/mods";

        System.out.println("=== KIỂM TRA TOÀN BỘ CLASS KHI HOTAI NẠP VÀO GAME ===");

        // Index jar classes
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

        Pattern zhPattern = Pattern.compile("[\u4e00-\u9fff]");
        int totalChecked = 0;
        int activeChineseClasses = 0;

        List<Path> badiffFiles = new ArrayList<>();
        Files.walkFileTree(Paths.get(hotaiDir), new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult visitFile(Path file, java.nio.file.attribute.BasicFileAttributes attrs) {
                if (file.toString().endsWith(".badiff") && !file.toString().endsWith(".bak")) {
                    badiffFiles.add(file);
                }
                return FileVisitResult.CONTINUE;
            }
        });

        for (Path badiffPath : badiffFiles) {
            Path rel = Paths.get(hotaiDir).relativize(badiffPath);
            String relStr = rel.toString().replace('\\', '/');
            String clzName = relStr.substring(0, relStr.length() - ".badiff".length()) + ".class";

            Path jarPath = classToJar.get(clzName);
            if (jarPath == null) continue;

            byte[] origBytes = null;
            try (ZipFile zf = new ZipFile(jarPath.toFile())) {
                ZipEntry ze = zf.getEntry(clzName);
                if (ze != null) origBytes = zf.getInputStream(ze).readAllBytes();
            }
            if (origBytes == null) continue;

            MemoryDiff diff = new MemoryDiff();
            try (InputStream is = Files.newInputStream(badiffPath)) {
                diff.deserialize(DefaultSerialization.newInstance(), is);
            } catch (Exception e) { continue; }

            byte[] patchedBytes;
            try {
                patchedBytes = MemoryDiffs.apply(origBytes, diff);
            } catch (Exception e) { continue; }

            totalChecked++;

            // Check if patchedBytes contains Chinese LDC strings
            try {
                ClassReader cr = new ClassReader(patchedBytes);
                ClassNode cn = new ClassNode();
                cr.accept(cn, 0);

                List<String> foundStrings = new ArrayList<>();
                for (MethodNode mn : cn.methods) {
                    for (AbstractInsnNode insn : mn.instructions) {
                        if (insn instanceof LdcInsnNode ldc && ldc.cst instanceof String str) {
                            if (zhPattern.matcher(str).find()) {
                                foundStrings.add(str);
                            }
                        }
                    }
                }

                if (!foundStrings.isEmpty()) {
                    activeChineseClasses++;
                    System.out.println("[CHINESE IN RUNTIME CLASS] " + clzName + ":");
                    for (String s : foundStrings) {
                        System.out.println("   -> \"" + s + "\"");
                    }
                }
            } catch (Exception e) {}
        }

        System.out.println("\n=== KẾT QUẢ KIỂM TRA RUNTIME HOTAI ===");
        System.out.println("Tổng số class đã kiểm tra: " + totalChecked);
        System.out.println("Số class còn chứa chuỗi tiếng Trung khi chạy trong game: " + activeChineseClasses);
    }
}
