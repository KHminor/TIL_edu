import java.io.*;
import java.util.*;

public class bj_2442 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        starPrints(n, bw);
        bw.flush();
        bw.close();
    }

    public static void starPrints(int n, BufferedWriter bw) throws IOException {
        for (int i=0; i<n; i++) {
            for (int j=n-1; j>=0; j--) {
                if (j>i) bw.write(" ");
                else bw.write("*");
            }
            for (int x=0; x<i; x++) {
                bw.write("*");
            }
            bw.write("\n");
        }
    }
}
