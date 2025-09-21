import java.io.*;
import java.util.*;

public class sw_2070 {
    public static void main(String[] agrs) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        for (int i=1; i<=t; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            bw.write(String.format("#%d %s", i,comparison(a,b))+'\n');
        }
        bw.flush();
        bw.close();
    }

    public static String comparison(int a, int b) {
        if (a>b) return ">";
        else if (a<b) return "<";
        else return "=";
    }
}
