import java.io.*;
import java.util.*;

public class _2110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] li = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = li[0];
        int c = li[1];

        // 집 위치 체크
        int[] check = new int[n];
        for (int i=0; i<n; i++) check[i] = Integer.parseInt(br.readLine());
        Arrays.sort(check);

        // 거리 차 간 사이 값 배열 생성
        int[] dist = java.util.stream.IntStream.rangeClosed(check[0],check[check.length-1]).toArray();

        // 이분 탐색 시작
        int[] result_li = new int[c];
        B_Search(check,dist, c, result_li);

        int result = 1000000000;
        for (int i=1; i<result_li.length; i++) result = Math.min(result, result_li[i]-result_li[i-1]);
        System.out.println(result);

    }

    public static void B_Search(int[] check, int[] dist, int c, int[] result_li) {
        // 이분 탐색 시작
        int s = 0;
        int e = dist.length-1;

        while (s<=e) {
            int m = (s+e)/2;
            int now_allow = check[0]+dist[m]-1;
            result_li[0] = check[0];
            int cnt = 1;
            for (int num: check) {
                if (num>now_allow) {
                    result_li[cnt] = num;
                    cnt++;
                    if (cnt>=c) break;
                    now_allow = num+dist[m]-1;
                }
            }
            if (cnt == c) break;
            else if (cnt > c) s = m;
            else e = m;
        }
    }
}
