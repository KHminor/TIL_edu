import java.io.*;
import java.util.*;

public class bj_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] result = {10000000,-10000000};
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            result[0] = Integer.min(result[0], num);
            result[1] = Integer.max(result[1], num);
        }
        System.out.printf("%d %d",result[0],result[1]);
    }
}
