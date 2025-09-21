import java.io.*;
import java.util.*;

public class sw_2058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] N = br.readLine().split("");
        System.out.println(hap(N));
    }

    public static int hap(String[] N) {
        int result = 0;
        for (int i=0; i<N.length; i++) {
            result += Integer.parseInt(N[i]);
        }
        return result;
    }
}
