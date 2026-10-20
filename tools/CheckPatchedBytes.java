import java.io.*;
import java.nio.file.*;
import java.util.zip.*;
import java.util.regex.*;
import org.badiff.*;
import org.badiff.imp.*;
import org.badiff.io.*;

public class CheckPatchedBytes {
    public static void main(String[] args) throws Exception {
        String baseDir = "D:/minecraft mod trung/Immersive Fight 4.2.9 Viet Hoa";
        String clzName = "com/latxx/fight_more/events/SculkWardenSummoner.class";
        Path jarPath = Paths.get(baseDir, "mods", "fight_more-1.0.jar");
        Path badiffPath = Paths.get(baseDir, "hotai", "com", "latxx", "fight_more", "events", "SculkWardenSummoner.badiff");

        byte[] origBytes;
        try (ZipFile zf = new ZipFile(jarPath.toFile())) {
            ZipEntry ze = zf.getEntry(clzName);
            origBytes = zf.getInputStream(ze).readAllBytes();
        }

        MemoryDiff diff = new MemoryDiff();
        try (InputStream is = Files.newInputStream(badiffPath)) {
            diff.deserialize(DefaultSerialization.newInstance(), is);
        }

        byte[] patched = MemoryDiffs.apply(origBytes, diff);
        String text = new String(patched, "UTF-8");
        Matcher m = Pattern.compile("[\u4e00-\u9fff]").matcher(text);
        int count = 0;
        while (m.find()) count++;
        System.out.println("Chinese characters in RESULTING PATCHED CLASS: " + count);
    }
}
