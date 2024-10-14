import java.io.*;
import java.util.*;
public class _15723 {
    static Deque<String> dq = new ArrayDeque<>();
    static Map<String,List<String>> dic;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        dic = new HashMap<>();

        int N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            String[] XY = br.readLine().split(" is ");
            String x = XY[0];
            String y = XY[1];
            if (!dic.containsKey(x)) dic.put(x,new ArrayList<>(Arrays.asList(y)));
            else dic.get(x).add(y);
        }

        int M = Integer.parseInt(br.readLine());
        for (int i=0; i<M; i++) {
            String[] XY = br.readLine().split(" is ");
            String x = XY[0];
            String y = XY[1];
            dq.add(x);
            bw.write(bfs(y)+"\n");
        }
        bw.flush();
    }

    public static String bfs(String end) {
        while (!dq.isEmpty()) {
            String now = dq.pollFirst();
            if (dic.containsKey(now)) {
                for (String alpha: dic.get(now)) {
                    if (alpha.equals(end)) return "T";
                    dq.add(alpha);
                }
            }
        }
        return "F";
    }
}
//3
//i is s
//s is t
//t is u
//3
//z is b
//c is b
//d is c