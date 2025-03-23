import java.io.*;
import java.util.*;

public class _10807 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(br.readLine());
        int result = 0;
        while (n-- != 0) {
            if (Integer.parseInt(st.nextToken())==v) result++;
        }
        System.out.println(result);
    }
}
