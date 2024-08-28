import java.io.*;
import java.util.*;

public class _sw_2070 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int i=1; i<=n; i++) {
            int[] li = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            String result = ">";
            if (li[0] == li[1]) result = "=";
            else if (li[0] < li[1]) result = "<";
            bw.write(String.format("#%d %s",i,result)+"\n");
        }
        bw.flush();
    }
}
