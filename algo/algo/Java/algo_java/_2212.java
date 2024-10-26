import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class _2212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        int[] li = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) li[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(li);
        Integer[] diff = new Integer[N-1];
        for (int i=0; i<N-1; i++) diff[i] = li[i+1]-li[i];
        Arrays.sort(diff, Collections.reverseOrder());
        // 즉, 센서간 차이를 내림차순으로 정렬 후, 집중국 개수 -1 부터 끝까지 더하면 결과로 나옴
        // 이유는 센서간 차이가 큰 공간을 기준으로, 집중국을 구분해야 최소의 합이 나오기 때문.
        int result = 0;
        for (int i=K-1; i<N-1; i++) result += diff[i];
        System.out.println(result);
    }
}
