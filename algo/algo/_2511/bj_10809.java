import java.io.*;
import java.util.*;

public class bj_10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] result = new int[26];
        Arrays.fill(result, -1);
        char[] li = br.readLine().toCharArray();
        for (int i=0; i<li.length; i++) {
            int num = li[i]-97;
            if (result[num]==-1) result[num] = i;
        }
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<result.length; i++) {
            if (i!=result.length-1) {
                sb.append(result[i]+" ");
            } else sb.append(result[i]);
        }
        System.out.println(sb);
    }
}
