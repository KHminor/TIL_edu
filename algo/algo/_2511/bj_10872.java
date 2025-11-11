import java.io.*;
import java.util.*;

public class bj_10872 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long result = 1L;
        int n = Integer.parseInt(br.readLine());
        for (int i=1; i<=n; i++) result*=i;
        System.out.println(result);
    }
}
