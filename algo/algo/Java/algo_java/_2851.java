import java.io.*;

public class _2851 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int[] li = new int[11];
//        for (int i=1; i<=10; i++) {
//            int num = Integer.parseInt(br.readLine());
//            li[i] = li[i-1]+num;
//        }
//        int result = 0;
//        for (int num: li) {
//            if (Math.abs(100-num) <= Math.abs(100-result)) result = num;
//        }
//        System.out.println(result);
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        boolean state = false;
        for (int i=0; i<10; i++) {
            int num = Integer.parseInt(br.readLine());
            if (!state && Math.abs(100-result)>=Math.abs(100-(result+num))) result += num;
            else state = true;

        }
        System.out.println(result);
    }
}
