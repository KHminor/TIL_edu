import java.io.*;
import java.util.*;

public class _30804 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
//    static int[][] li;
//    public static void main(String[] args) throws IOException {
//        int N = Integer.parseInt(br.readLine());
//        addFruits(N);
//        System.out.println(findManyFruits(N));
//    }

//    private static void addFruits(int N) throws IOException {
//        li = new int[N+1][10];
//        st = new StringTokenizer(br.readLine());
//        for (int i=1; i<=N; i++) {
//            li[i]= Arrays.stream(li[i-1]).toArray();
//            li[i][Integer.parseInt(st.nextToken())]++;
//        }
//    }
//
//    private static int findManyFruits(int N) {
//        int result = 0;
//        for (int i=1; i<N; i++) { // 기준
//            for (int j=i+1; j<=N; j++) { // 이동
//                int[] f_cnt = {0,0}; // 과일 종류, 총 개수
//                for (int k=0; k<9; k++) {
//                    if (li[j][k]-li[i-1][k]!=0) {
//                        f_cnt[0]++; // 과일 카운팅
//                        f_cnt[1]+=li[j][k]-li[i-1][k]; // 총 개수 카운팅
//                        if (f_cnt[0]>2) break;
//                    }
//                }
//                if (!(f_cnt[0]>2)&&f_cnt[1]>result) result=f_cnt[1];
//            }
//        }
//        return result;
//    }

    static int[] li;
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        addFruits(N);
        System.out.println(findManyFruits(N));
    }


    private static void addFruits(int N) throws IOException {
        li = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) li[i]=Integer.parseInt(st.nextToken());
    }

    private static int findManyFruits(int N) {
        Map<Integer, Integer> fruits = new HashMap<>();
        int result = 0;
        int s = 0;
        for (int e=0; e<N; e++) {
            fruits.put(li[e],fruits.getOrDefault(li[e],0)+1);
            while (fruits.size()>2) {
                fruits.put(li[s],fruits.get(li[s])-1);
                if (fruits.get(li[s])==0) fruits.remove(li[s]);
                s++;
            }
            if (e-s+1>result) result = e-s+1;
        }
        return result;
    }
}