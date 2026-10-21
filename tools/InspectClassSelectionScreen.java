import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;
import org.objectweb.asm.*;
import org.objectweb.asm.tree.*;

public class InspectClassSelectionScreen {
    public static void main(String[] args) throws Exception {
        String jarPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/mods/class_enhancement-0.1.jar";
        String badiffPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/hotai/com/misanthropy/linggango/class_enhancement/client/ClassSelectionScreen.badiff";
        
        byte[] origBytes = null;
        try (ZipFile zf = new ZipFile(jarPath)) {
            ZipEntry ze = zf.getEntry("com/misanthropy/linggango/class_enhancement/client/ClassSelectionScreen.class");
            try (InputStream is = zf.getInputStream(ze)) {
                origBytes = is.readAllBytes();
            }
        }
        
        System.out.println("Orig class size: " + origBytes.length);
        
        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(Paths.get(badiffPath))) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }
        byte[] patchedBytes = MemoryDiffs.apply(origBytes, diff);
        System.out.println("Patched class size: " + patchedBytes.length);
        
        ClassReader cr = new ClassReader(patchedBytes);
        ClassNode cn = new ClassNode();
        cr.accept(cn, 0);
        
        for (MethodNode mn : cn.methods) {
            for (AbstractInsnNode insn : mn.instructions) {
                if (insn instanceof LdcInsnNode) {
                    LdcInsnNode ldc = (LdcInsnNode) insn;
                    if (ldc.cst instanceof String) {
                        System.out.println("LDC [" + mn.name + "]: " + ldc.cst);
                    }
                }
            }
        }
    }
}
