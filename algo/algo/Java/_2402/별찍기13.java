import java.io.*;

public class 별찍기13 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i < 2*n; i++) {
            if (i <= n) for (int j = 0; j < i; j++) System.out.print("*");
            else for (int j = 0; j < 2 * n - i; j++) System.out.print("*");
            System.out.println();
        }
    }
}
