import java.io.*;

public class _10798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[][] mtx = new char[5][15];
        for (int i=0; i<5; i++) {
            char[] li = br.readLine().toCharArray();
            for (int j=0; j<li.length; j++) mtx[i][j] = li[j];
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<15; i++) {
            for (int j=0; j<5; j++) {
                if (mtx[j][i]!=0) {
                    sb.append(mtx[j][i]);
                }
            }
        }
        System.out.println(sb);
    }
}
