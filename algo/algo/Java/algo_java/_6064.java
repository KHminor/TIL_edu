import java.io.*;
import java.util.*;

public class _6064 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T>0) {
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (x>y) {
                int tmp1 = M;
                int tmp2 = x;
                M = N;
                x = y;
                N = tmp1;
                y = tmp2;
            }

            int result = findKaing(M,N,x,y);
            bw.write(result+"\n");
            T--;
        }
        bw.flush();
    }

    private static int findKaing(int M, int N, int x, int y) {
        Set<Integer> s_li = new HashSet<>(Arrays.asList(x));
        int cnt = x;
        int now = x;
        boolean state = false;
        if (x!=y) {
            while (true) {
                now=(now+M)%N==0?N:(now+M)%N;
                cnt+=M;
                if (now==y) {
                    state = true;
                    break;
                } else if (s_li.contains(now)) break;
                s_li.add(now);
            }
        } else state = true;
        return state?cnt:-1;
    }
}


// 10 12 3 9
// 1 1 -> 3 3 -> 13 13 (3 1) -> 13 11 -> (3 11) -> 13 21 (3 9)

// 10 12 7 2
// 12 10 2 7
// 1 1 -> 2 2 [2]-> 14 14 (2 4) [14]-> 14 16 (2 6) [26]-> 14 18 (2 8) -> 14 20 (2 10) -> 14 22(2 2) -> 14 14 (2 2