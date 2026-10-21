import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

jdk_bin = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\jre\java-runtime-gamma\windows-x64\java-runtime-gamma\bin"
javac = os.path.join(jdk_bin, "javac.exe")
java = os.path.join(jdk_bin, "java.exe")

asm_jar = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm\9.10.1\asm-9.10.1.jar"
asm_tree_jar = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm-tree\9.10.1\asm-tree-9.10.1.jar"
hotai_jar = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\mods\hotai-1.0.jar"
tools_dir = r"D:\minecraft mod trung\tools"

classpath = f"{asm_jar};{asm_tree_jar};{hotai_jar};{tools_dir}"

java_code = """import java.io.*;
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
"""

with open(os.path.join(tools_dir, "InspectClassSelectionScreen.java"), "w", encoding="utf-8") as f:
    f.write(java_code)

res = subprocess.run([javac, "-cp", classpath, "-encoding", "UTF-8", "InspectClassSelectionScreen.java"], cwd=tools_dir, capture_output=True, text=True)
if res.returncode != 0:
    print("Compile error:", res.stderr)
    sys.exit(1)

res = subprocess.run([java, "-cp", classpath, "-Dfile.encoding=UTF-8", "InspectClassSelectionScreen"], cwd=tools_dir, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
