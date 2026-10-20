import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

public class TestSingleFile {
    public static void main(String[] args) throws Exception {
        String baseDir = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa";
        String clzName = "com/latxx/fight_more/events/SculkWardenSummoner.class";
        Path jarPath = Paths.get(baseDir, "mods", "fight_more-1.0.jar");
        Path badiffPath = Paths.get(baseDir, "hotai", "com", "latxx", "fight_more", "events", "SculkWardenSummoner.badiff");

        byte[] origBytes;
        try (ZipFile zf = new ZipFile(jarPath.toFile())) {
            ZipEntry ze = zf.getEntry(clzName);
            try (InputStream is = zf.getInputStream(ze)) {
                origBytes = is.readAllBytes();
            }
        }

        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(badiffPath)) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }

        byte[] patched = MemoryDiffs.apply(origBytes, diff);
        ClassReader cr = new ClassReader(patched);
        ClassNode cn = new ClassNode();
        cr.accept(cn, 0);

        System.out.println("Class: " + cn.name);
        for (MethodNode mn : cn.methods) {
            System.out.println("Method: " + mn.name + mn.desc);
            for (AbstractInsnNode insn : mn.instructions) {
                if (insn instanceof LdcInsnNode ldc) {
                    System.out.println("  LDC: " + ldc.cst + " (" + (ldc.cst != null ? ldc.cst.getClass() : "null") + ")");
                }
            }
        }
    }
}
