import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

public class PatchModifierToVietnamese {
    public static void main(String[] args) throws Exception {
        String jarPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/mods/Modifiers-forge-1.20.1-0.1.3.jar";
        String badiffPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/hotai/cursedflames/modifiers/common/modifier/Modifier.badiff";

        // 1. Read original bytes from jar
        byte[] origBytes;
        try (ZipFile zf = new ZipFile(jarPath)) {
            ZipEntry ze = zf.getEntry("cursedflames/modifiers/common/modifier/Modifier.class");
            try (InputStream is = zf.getInputStream(ze)) {
                origBytes = is.readAllBytes();
            }
        }

        // 2. Read diff and apply to get current patched class
        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(Paths.get(badiffPath))) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }
        byte[] currentPatched = MemoryDiffs.apply(origBytes, diff);

        // 3. Use ASM to replace Chinese strings in the bytecode
        Map<String, String> translations = new HashMap<>();
        translations.put("伤害", "Sát thương");
        translations.put("攻速", "Tốc độ đánh");
        translations.put("击退", "Đẩy lùi");
        translations.put("护甲值", "Giáp");
        translations.put("盔甲韧性", "Độ cứng giáp");
        translations.put("击退抗性", "Kháng đẩy lùi");
        translations.put("最大生命值", "Máu tối đa");
        translations.put("生命上限", "Máu tối đa");
        translations.put("幸运", "May mắn");
        translations.put("移速", "Tốc độ di chuyển");

        ClassReader cr = new ClassReader(currentPatched);
        ClassNode cn = new ClassNode();
        cr.accept(cn, 0);

        int replacedCount = 0;
        for (MethodNode mn : cn.methods) {
            for (AbstractInsnNode insn : mn.instructions) {
                if (insn instanceof LdcInsnNode ldc) {
                    if (ldc.cst instanceof String str) {
                        for (Map.Entry<String, String> entry : translations.entrySet()) {
                            if (str.equals(entry.getKey())) {
                                System.out.println("Replacing in " + mn.name + ": " + str + " -> " + entry.getValue());
                                ldc.cst = entry.getValue();
                                replacedCount++;
                            }
                        }
                    }
                }
            }
        }

        System.out.println("Total string constants replaced: " + replacedCount);

        ClassWriter cw = new ClassWriter(0);
        cn.accept(cw);
        byte[] vietnamesePatched = cw.toByteArray();

        // 4. Compute new badiff against original jar bytes
        MemoryDiff newDiff = MemoryDiffs.diff(origBytes, vietnamesePatched);

        // 5. Save back to badiff
        // Make backup first
        Path badiffP = Paths.get(badiffPath);
        Files.copy(badiffP, Paths.get(badiffPath + ".bak"), StandardCopyOption.REPLACE_EXISTING);

        try (OutputStream os = Files.newOutputStream(badiffP)) {
            newDiff.serialize(DefaultSerialization.newInstance(), os);
        }

        System.out.println("SUCCESS! New Vietnamese badiff saved to " + badiffPath);

        // 6. Verify by reading back and applying
        MemoryDiff verifyDiff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(badiffP)) {
            verifyDiff.deserialize(DefaultSerialization.newInstance(), is);
        }
        byte[] testApplied = MemoryDiffs.apply(origBytes, verifyDiff);
        if (Arrays.equals(testApplied, vietnamesePatched)) {
            System.out.println("VERIFICATION PASSED: Diff applies perfectly to produce desired bytecode!");
        } else {
            System.err.println("VERIFICATION FAILED: Mismatch in applied bytes!");
        }
    }
}
