import java.io.*;
import java.util.Arrays;

public class _sw_1285 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int tc = Integer.parseInt(br.readLine());
        int[] li = new int[100001];

        for (int t=1; t<=tc; t++) {
            int n = Integer.parseInt(br.readLine());
            int min_num = 100000;
            for (int num: Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray()) {
                int now = Math.abs(num);
                li[now]++;
                min_num = Math.min(now, min_num);
            }
            bw.write(String.format("#%d %d %d",t,min_num,li[min_num])+"\n");
        }
        bw.flush();
    }
}
