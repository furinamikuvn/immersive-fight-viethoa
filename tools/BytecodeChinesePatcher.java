import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;

public class BytecodeChinesePatcher {

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.out.println("Usage: BytecodeChinesePatcher <replacements.tsv> <jar_path>");
            return;
        }

        File tsvFile = new File(args[0]);
        File jarFile = new File(args[1]);

        if (!tsvFile.exists() || !jarFile.exists()) {
            System.err.println("File not found: " + tsvFile + " or " + jarFile);
            return;
        }

        Map<String, String> replacements = new LinkedHashMap<>();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(tsvFile), "UTF-8"))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.trim();
                if (line.isEmpty() || line.startsWith("#")) continue;
                String[] parts = line.split("\t");
                if (parts.length >= 2) {
                    replacements.put(parts[0], parts[1]);
                }
            }
        }

        System.out.println("Loaded " + replacements.size() + " replacement rules from " + tsvFile.getName());
        patchJar(jarFile, replacements);
    }

    public static void patchJar(File jarFile, Map<String, String> replacements) throws Exception {
        File tempJar = new File(jarFile.getAbsolutePath() + ".tmp");
        int patchedClasses = 0;
        int totalReplacedStrings = 0;

        try (ZipFile zipIn = new ZipFile(jarFile);
             ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(tempJar))) {

            Enumeration<? extends ZipEntry> entries = zipIn.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                byte[] data = readAllBytes(zipIn.getInputStream(entry));

                if (entry.getName().endsWith(".class")) {
                    try {
                        ClassReader cr = new ClassReader(data);
                        ClassNode cn = new ClassNode();
                        cr.accept(cn, 0);

                        boolean modified = false;

                        // Check fields
                        if (cn.fields != null) {
                            for (FieldNode fn : cn.fields) {
                                if (fn.value instanceof String) {
                                    String orig = (String) fn.value;
                                    String replaced = applyReplacements(orig, replacements);
                                    if (!replaced.equals(orig)) {
                                        fn.value = replaced;
                                        modified = true;
                                        totalReplacedStrings++;
                                    }
                                }
                            }
                        }

                        // Check methods
                        if (cn.methods != null) {
                            for (MethodNode mn : cn.methods) {
                                if (mn.instructions != null) {
                                    for (AbstractInsnNode insn : mn.instructions) {
                                        if (insn instanceof LdcInsnNode) {
                                            LdcInsnNode ldc = (LdcInsnNode) insn;
                                            if (ldc.cst instanceof String) {
                                                String orig = (String) ldc.cst;
                                                String replaced = applyReplacements(orig, replacements);
                                                if (!replaced.equals(orig)) {
                                                    ldc.cst = replaced;
                                                    modified = true;
                                                    totalReplacedStrings++;
                                                }
                                            }
                                        } else if (insn instanceof InvokeDynamicInsnNode) {
                                            InvokeDynamicInsnNode indy = (InvokeDynamicInsnNode) insn;
                                            if (indy.bsmArgs != null) {
                                                for (int i = 0; i < indy.bsmArgs.length; i++) {
                                                    if (indy.bsmArgs[i] instanceof String) {
                                                        String orig = (String) indy.bsmArgs[i];
                                                        String replaced = applyReplacements(orig, replacements);
                                                        if (!replaced.equals(orig)) {
                                                            indy.bsmArgs[i] = replaced;
                                                            modified = true;
                                                            totalReplacedStrings++;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }

                        if (modified) {
                            ClassWriter cw = new ClassWriter(0);
                            cn.accept(cw);
                            data = cw.toByteArray();
                            patchedClasses++;
                            System.out.println("  Patched class: " + entry.getName());
                        }
                    } catch (Exception e) {
                        // Skip if unparseable or obfuscated non-standard class
                    }
                }

                ZipEntry outEntry = new ZipEntry(entry.getName());
                zos.putNextEntry(outEntry);
                zos.write(data);
                zos.closeEntry();
            }
        }

        System.out.println("Finished patching " + jarFile.getName() + ": " + patchedClasses + " classes patched, " + totalReplacedStrings + " string replacements.");

        if (patchedClasses > 0) {
            jarFile.delete();
            tempJar.renameTo(jarFile);
            System.out.println("Successfully replaced " + jarFile.getName());
        } else {
            tempJar.delete();
            System.out.println("No changes needed in " + jarFile.getName());
        }
    }

    private static String applyReplacements(String text, Map<String, String> replacements) {
        String result = text;
        for (Map.Entry<String, String> entry : replacements.entrySet()) {
            if (result.contains(entry.getKey())) {
                result = result.replace(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }

    private static byte[] readAllBytes(InputStream is) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        byte[] buf = new byte[8192];
        int n;
        while ((n = is.read(buf)) != -1) {
            baos.write(buf, 0, n);
        }
        return baos.toByteArray();
    }
}
