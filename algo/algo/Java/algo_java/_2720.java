import java.io.*;
import java.util.Scanner;

public class _2720 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = sc.nextInt();
        int[] val = {25,10,5,1};
        while (T>0) {
            int cash = sc.nextInt();
            for (int v: val) {
                if (cash/v!=0) {
                    bw.write(cash/v+" ");
                    cash%=v;
                } else bw.write(0+" ");
            }
            bw.write("\n");
            T--;
        }
        bw.flush();
    }
}