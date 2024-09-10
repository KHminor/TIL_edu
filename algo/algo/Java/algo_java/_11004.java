import java.io.*;
import java.util.*;
public class _11004 {
    static int K;
    static int[] li;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        li = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) li[i] = Integer.parseInt(st.nextToken());
        quickSort(0,N-1);
        System.out.println(li[K-1]);
    }

//    public static void merge_sort(int s, int e, int ln) {
//        // devide
//        int mid = ln/2;
//        if (ln >= 2) {
//            merge_sort(s,mid,mid-s); // 앞
//            merge_sort(mid+1,e,e-(mid+1)); // 뒤
//        }
//        int f_idx = s;
//        int b_idx = mid+1;
//        for (int i=0; i<ln; i++) {
//            if (li[f_idx]>=li[b_idx]) {
//                int num = li[f_idx];
//                li[f_idx] = li[b_idx];
//                li[b_idx] = num;
//                b_idx++;
//            } else f_idx++;
//        }
//    }

    // 퀵 정렬 메서드
    public static void quickSort(int low, int high) {
        if (low < high) {
            // 피벗을 기준으로 배열을 분할하고 피벗의 인덱스를 반환
            int pi = partition(low, high);

            // 피벗을 기준으로 좌우 부분 배열을 재귀적으로 정렬
            quickSort(low, pi - 1);  // 왼쪽 부분
            quickSort(pi + 1, high); // 오른쪽 부분
        }
    }

    // 배열을 피벗 기준으로 분할하는 메서드
    public static int partition( int low, int high) {
        int pivot = li[high];  // 마지막 요소를 피벗으로 선택
        int i = (low - 1); // 작은 요소를 추적할 인덱스

        for (int j = low; j < high; j++) {
            // 현재 요소가 피벗보다 작거나 같은 경우
            if (li[j] <= pivot) {
                i++;
                // li[i]와 li[j]를 교환
                int temp = li[i];
                li[i] = li[j];
                li[j] = temp;
            }
        }

        // 피벗을 올바른 위치로 이동
        int temp = li[i + 1];
        li[i + 1] = li[high];
        li[high] = temp;

        return i + 1;  // 피벗의 인덱스를 반환
    }
}
