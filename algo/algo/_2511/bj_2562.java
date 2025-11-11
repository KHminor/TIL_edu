import java.io.*;
import java.util.*;

public class bj_2562 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] result = new int[]{0,1};
        int n = 1;
        while (n<=9) {
            int x = Integer.parseInt(br.readLine());
            if (x>result[1]) {
                result = new int[]{n,x};
            }
            n++;
        }
        System.out.println(result[1]);
        System.out.println(result[0]);
    }
}
