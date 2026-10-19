import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

public class TestSingle {
    public static void main(String[] args) throws Exception {
        String jarPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/mods/relics-1.20.1-0.8.0.7.jar";
        String badiffPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/hotai/it/hurts/sskirillss/relics/items/relics/MagicMirrorItem.badiff";

        byte[] orig;
        try (ZipFile zf = new ZipFile(jarPath)) {
            ZipEntry ze = zf.getEntry("it/hurts/sskirillss/relics/items/relics/MagicMirrorItem.class");
            try (InputStream is = zf.getInputStream(ze)) {
                orig = is.readAllBytes();
            }
        }

        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(Paths.get(badiffPath))) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }

        byte[] currentPatched = MemoryDiffs.apply(orig, diff);
        ClassReader cr = new ClassReader(currentPatched);
        ClassNode cn = new ClassNode();
        cr.accept(cn, 0);

        for (MethodNode mn : cn.methods) {
            for (AbstractInsnNode insn : mn.instructions) {
                if (insn instanceof LdcInsnNode ldc && ldc.cst instanceof String str) {
                    System.out.println("Ldc in " + mn.name + ": " + str);
                }
            }
        }
    }
}
