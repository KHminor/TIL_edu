import java.io.*;
import java.util.*;
import java.util.stream.*;

public class bj_1158 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("<");
        String[] NK = br.readLine().split(" ");
        int N = Integer.parseInt(NK[0]);
        int n_N = N;
        int K = Integer.parseInt(NK[1]);

        ArrayList<Integer> arr = IntStream.rangeClosed(1,N).boxed().collect(Collectors.toCollection(ArrayList::new));
        int now = -1;
        for (int i=0; i<N; i++) {
            now = (now+K)%n_N;
            bw.write(String.valueOf(arr.get(now)));
            arr.remove(now--);
            n_N--;
            if (n_N!=0) {
                bw.write(", ");
            }
        }
        bw.write(">");
        bw.flush();
        bw.close();
    }
}
