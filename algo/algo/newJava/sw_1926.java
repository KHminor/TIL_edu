import java.io.*;
import java.util.*;

public class sw_1926 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb;
        int N = Integer.parseInt(br.readLine());

        Set<Character> target = new HashSet<Character>(){{
            add('3');
            add('6');
            add('9');
        }};

        for (int i=1; i<=N; i++) {
            char[] li = String.valueOf(i).toCharArray();
            sb = new StringBuilder();
            boolean isTarget = false;
            for (int j=0; j<li.length; j++) {
                if (target.contains(li[j])) {
                    if (!isTarget) {
                        isTarget = true;
                        sb = new StringBuilder();
                    }
                    sb.append("-");
                } else if (!isTarget) {
                    sb.append(li[j]);
                }
            }
            bw.write(sb.toString()+" ");
        }
        bw.flush();
        bw.close();

    }
}
