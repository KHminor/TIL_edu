import java.io.*;

public class sw_2046 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        while (N!=0) {
            sb.append("#");
            N--;
        }
        System.out.println(sb);
    }
}
