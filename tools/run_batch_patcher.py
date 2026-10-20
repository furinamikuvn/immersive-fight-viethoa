import os
import subprocess
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

jdk_bin = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\jre\java-runtime-gamma\windows-x64\java-runtime-gamma\bin"
javac = os.path.join(jdk_bin, "javac.exe")
java = os.path.join(jdk_bin, "java.exe")

asm_jar = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm\9.10.1\asm-9.10.1.jar"
asm_tree_jar = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm-tree\9.10.1\asm-tree-9.10.1.jar"
hotai_jar = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\mods\hotai-1.0.jar"

classpath = f"{asm_jar};{asm_tree_jar};{hotai_jar};."

tools_dir = r"D:\minecraft mod trung\tools"

print("1. Bien dich BatchPatchAllHotaiBadiffs.java...")
res = subprocess.run([javac, "-cp", classpath, "-encoding", "UTF-8", "BatchPatchAllHotaiBadiffs.java"], cwd=tools_dir, capture_output=True, text=True)
if res.returncode != 0:
    print("Compile error:", res.stderr)
    sys.exit(1)
print("Bien dich thanh cong!")

print("2. Chay BatchPatchAllHotaiBadiffs...")
res = subprocess.run([java, "-cp", classpath, "-Dfile.encoding=UTF-8", "BatchPatchAllHotaiBadiffs"], cwd=tools_dir, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

print("Hoan tat chay patch bytecode!")
