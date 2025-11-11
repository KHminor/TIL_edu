import java.io.*;

public class bj_2576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] result = {0,99};
        int N = 7;
        while (N>=1) {
            int x = Integer.parseInt(br.readLine());
            if (x%2!=0) {
                result[0]+=x;
                result[1] = Integer.min(result[1],x);
            }
            N--;
        }
        if (result[0]!=0) {
            System.out.println(result[0]);
            System.out.println(result[1]);
        } else {
            System.out.println(-1);
        }
    }
}
