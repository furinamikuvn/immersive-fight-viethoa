import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;

public class ApplyBadiff {
    public static void main(String[] args) throws Exception {
        String jarPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/mods/Modifiers-forge-1.20.1-0.1.3.jar";
        String badiffPath = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa/hotai/cursedflames/modifiers/common/modifier/Modifier.badiff";
        String outPath = "D:/minecraft mod trung/tools/PatchedModifier.class";

        byte[] origBytes = null;
        try (ZipFile zf = new ZipFile(jarPath)) {
            ZipEntry ze = zf.getEntry("cursedflames/modifiers/common/modifier/Modifier.class");
            try (InputStream is = zf.getInputStream(ze)) {
                origBytes = is.readAllBytes();
            }
        }

        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(Paths.get(badiffPath))) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }
        byte[] patchedBytes = org.badiff.MemoryDiffs.apply(origBytes, diff);

        Files.write(Paths.get(outPath), patchedBytes);
        System.out.println("Patched class written to " + outPath + " (size: " + patchedBytes.length + " bytes)");
    }
}
