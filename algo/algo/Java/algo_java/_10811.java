import java.io.*;
import java.util.*;
import java.util.stream.*;

public class _10811 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<Integer> n_li = new ArrayList<>(Arrays.asList(IntStream.rangeClosed(1,n).boxed().toArray(Integer[]::new)));
        while (m--!=0) {
            ArrayList<Integer> li = new ArrayList<>(n_li);
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            for (int k=i; k<=j; k++) {
                li.set(k-1,n_li.get(j+i-k-1));
            }
            n_li = new ArrayList<>(li);
        }
        System.out.println(n_li.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }
}

// [0, 2, 1, 4, 3, 5]
