import java.io.*;
import java.util.*;
public class bj_3460 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++) {
            int n = Integer.parseInt(br.readLine());
            find_num(n,1);
        }
    }

    public static void find_num(int n, int now) {
        StringBuilder sb = new StringBuilder();
        int cnt = 1;
        while (n>=now*2) {
            now*=2;
            cnt++;
        }
        int[] result = new int[cnt];
        Arrays.fill(result, -1);
        for (int i=cnt-1; i>=0; i--) {
            if (n-now>=0) {
                result[i]=i;
                n-=now;
            }
            now/=2;
        }
        for (int idx: result) {
            if (idx!=-1) sb.append(idx+" ");
        }
        System.out.println(sb);
    }
}
