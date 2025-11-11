import java.io.*;
import java.util.*;

public class bj_1037 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] li = new int[N];
        for (int i=0; i<N; i++) {
            li[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(li);
        if (li.length >= 1) System.out.println(li[0]*li[li.length-1]);
        else System.out.println(Math.pow(li[0],2));
    }
}
