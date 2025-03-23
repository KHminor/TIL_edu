import java.io.*;
import java.util.*;

public class _10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int mx = Integer.MIN_VALUE;
        int mn = Integer.MAX_VALUE;
        for (int i=0; i<n; i++) {
            int num = Integer.parseInt(st.nextToken());
            mx = Math.max(mx,num);
            mn = Math.min(mn,num);
        }
        System.out.print(mn + " " + mx);
    }
}
