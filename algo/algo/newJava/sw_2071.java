import java.io.*;
import java.util.*;

public class sw_2071 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        for (int i=1; i<=t; i++) {
            st = new StringTokenizer(br.readLine());
            bw.write(String.format("#%d %d", i, average(st))+"\n");
        }
        bw.flush();
        bw.close();
    }

    public static int average(StringTokenizer st) {
        double result = 0L;
        while (st.hasMoreTokens()) {
            result += Double.parseDouble(st.nextToken());
        }
        return (int)Math.round(result/10L);
    }
}
