import java.io.*;
import java.util.*;

public class bj_2441 {
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
            for (int j=n; j>=1; j--) {
                if (j>i) bw.write(" ");
                else bw.write("*");
            }
            bw.write("\n");
        }
    }
}
