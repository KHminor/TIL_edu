import java.io.*;
import java.util.*;

public class bj_2440 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        starPrints(n, bw);
        bw.flush();
        bw.close();
    }

    public static void starPrints(int n, BufferedWriter bw) throws IOException {
        for (int i=n; i>=1; i--) {
            for (int j=1; j<=n; j++) {
                if (i>=j) {
                    bw.write("*");
                } else break;
            }
            bw.write("\n");
        }
    }
}
