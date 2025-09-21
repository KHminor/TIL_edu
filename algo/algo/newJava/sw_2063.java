import java.io.*;
import java.util.*;

public class sw_2063 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        System.out.println(mid(st, N));
    }

    public static int mid(StringTokenizer st, int N) {
        int[] li = new int[N];
        for (int i=0; i<N; i++) li[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(li);
        return li[N/2];
    }
}
