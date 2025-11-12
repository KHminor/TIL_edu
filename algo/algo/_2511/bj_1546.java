import java.io.*;
import java.util.*;

public class bj_1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int mx = 0;
        int hap = 0;
        int[] li = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            int x = Integer.parseInt(st.nextToken());
            li[i] = x;
            hap+=x;
            mx = Integer.max(mx, x);
        }

        float result = hap/(float)mx*100;
        System.out.println(result/N);
    }
}
// 50