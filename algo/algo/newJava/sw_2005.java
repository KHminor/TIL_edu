import java.io.*;
import java.util.*;

public class sw_2005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw;
        int T = Integer.parseInt(br.readLine());
        for (int i=1; i<=T; i++) {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
            int N = Integer.parseInt(br.readLine());
            int[][] arr = new int[N][N];
            arr[0][0] = 1;
            bw.write(String.format("#%d\n",i));
            bw.write("1"+"\n");

            for (int a=1; a<N; a++) {
                for (int b=0; b<=a; b++) {
                    if (checkNum(b-1,a)) {
                        arr[a][b]+=arr[a-1][b-1];
                    }
                    if (checkNum(b,a)) {
                        arr[a][b]+=arr[a-1][b];
                    }
                    bw.write(arr[a][b]+" ");
                }
                bw.write("\n");
            }
            bw.flush();
        }
    }

    public static boolean checkNum(int x, int a) {
        return 0 <= x && x < a;
    }
}
