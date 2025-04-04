import java.io.*;
import java.util.*;

public class _2738_2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int[][] mtx = new int[n][m];
        mtxAdd(mtx);
        printMtx(mtx);
    }

    public static void mtxAdd(int[][] mtx) throws IOException {
        for (int t=0; t<2; t++) {
            for (int i=0; i<n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<m; j++) mtx[i][j]+=Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void printMtx(int[][] mtx) {
       StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) sb.append(mtx[i][j]).append(" ");
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
