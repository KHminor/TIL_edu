import java.io.*;
import java.util.*;

public class sw_1859
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i=1; i<=T; i++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            long result = 0L;
            int before = 0;
            for (int j=arr.length-1; j>=0; j--) {
                if (arr[j]>=before) before=arr[j];
                else result+=before-arr[j];
            }
            bw.write(String.format("#%d %d", i, result)+"\n");
        }
        bw.flush();
        bw.close();
    }
}