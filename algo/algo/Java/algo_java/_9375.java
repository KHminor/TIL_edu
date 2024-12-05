import java.io.*;
import java.util.*;

public class _9375 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static Map<String, Set<String>> dic;
    public static void main(String[] args) throws IOException {

        int T = Integer.parseInt(br.readLine());
        while (T>0) {
            dic = new HashMap<>();
            int N = Integer.parseInt(br.readLine());
            addMap(N);
            bw.write(counting()+"\n");
            T--;
        }
        bw.flush();
    }

    private static void addMap(int N) throws IOException {
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String v = st.nextToken();
            String k = st.nextToken();
            if (!dic.containsKey(k)) dic.put(k,new HashSet<>(Arrays.asList(v)));
            else dic.get(k).add(v);
        }
    }

    private static int counting() {
        int result = 1;
        for (Set<String> li: dic.values()) result*=li.size()+1;
        return result-1;
    }
}

// 1 2 3
// 4 5
// 6 7

// 1 2 3 4 5 6 7 = 7
// 14 15 16 17, 24 25 26 27, 34 35 36 37,  46 47, 56 57 = 16
// 146 147 156 157, = 12

// 35 = > 7+12+(6+6+4)16