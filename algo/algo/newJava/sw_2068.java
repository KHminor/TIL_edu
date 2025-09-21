import java.io.*;
import java.util.*;

public class sw_2068 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine().strip());
        for (int i=1; i<=t; i++) {
            st = new StringTokenizer(br.readLine());
            bw.write(String.format("#%d %d", i, max(st))+"\n");
        }
        bw.flush();
        bw.close();
    }

    public static int max(StringTokenizer st) {
        int result = 0;
        while (st.hasMoreTokens()) {
            int x = Integer.parseInt(st.nextToken());
            if (result<x) result = x;
        }
        return result;
    }
}
