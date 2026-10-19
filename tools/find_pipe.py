import os
import zipfile
import glob

mods_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\mods"
for jar in glob.glob(os.path.join(mods_dir, "*.jar")):
    try:
        with zipfile.ZipFile(jar, "r") as zf:
            for name in zf.namelist():
                if name.endswith(".class"):
                    data = zf.read(name)
                    if b" | " in data:
                        print(f"{os.path.basename(jar)} -> {name}")
    except Exception as e:
        pass
