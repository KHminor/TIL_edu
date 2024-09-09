import java.io.*;
import java.util.stream.*;

public class _21756 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int n = Integer.parseInt(br.readLine());
//        int[] li = IntStream.rangeClosed(1,n).toArray();
//        while (n!=1) {
//            int cnt = 0;
//            int[] arr = new int[n/2];
//            for (int i=1; i<n; i+=2) {
//                arr[cnt] = li[i];
//                cnt++;
//            }
//            li = arr;
//            n = cnt;
//        }
//        System.out.println(li[0]);
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 1;
        for (int i=1; i<=6; i++) {
            int val = (int)Math.pow(2,i);
            if (val<= n) result = val;
            else break;
        }
        System.out.println(result);
    }
}

// ln =
// 1 2 3 4 5 6 7 8 9 10
// 2 4 6 8 10  2(1)
// 4 8 2(2)
// 8 2(3)