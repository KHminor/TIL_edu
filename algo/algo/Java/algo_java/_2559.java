import java.util.Arrays;
import java.util.Scanner;

public class _2559 {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int N = sc.nextInt();
//        int K = sc.nextInt();
//        int[] li = new int[N];
//        li[0]=sc.nextInt();
//        for (int i=1; i<N; i++) {
//            li[i]=li[i-1]+sc.nextInt();
//        }
//        int mx = li[K-1];
//        for (int i=0; i<N-K; i++) {
//            mx = Math.max(mx,li[i+K]-li[i]);
//        }
//        System.out.println(mx);
//    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] li = new int[N];
        int[] check = new int[N+1];
        for (int i=0; i<N; i++) {
            li[i]=sc.nextInt();
            check[i+1]=li[i]+check[i];
        }
        System.out.println(Arrays.toString(check));
        int result = Integer.MIN_VALUE;
        for (int i=0; i<=N-K; i++) {
            System.out.println(check[i + K]);
            System.out.println(check[i]);
            result = Math.max(result, check[i + K] - check[i]);
            System.out.println("===========");
        }
        System.out.println(result);
    }
}
