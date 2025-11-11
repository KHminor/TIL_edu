import java.io.*;

public class bj_5598 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        char[] br_li = br.readLine().toCharArray();
        for (char x : br_li) {
            int n = x;
            if (n-3 <65) sb.append((char) (n-3+26));
            else sb.append((char) (n-3));
        }
        System.out.println(sb);
    }
}
