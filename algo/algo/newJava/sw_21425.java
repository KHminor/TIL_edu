import java.io.*;
import java.util.*;

public class sw_21425 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        while (T!=0) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            if (x>y) {
                int moc = x;
                x=y;
                y=moc;
            }
            bw.write(result(x,y,N)+"\n");
            T--;
        }
        bw.flush();
        bw.close();

    }

    public static int result(int x, int y, int N) {
        int result = 0;
        int hap = 0;
        while (hap<=N) {
            hap = x+y;
            if (result%2==0) {
                x+=y;
            } else {
                y+=x;
            }
            result++;
        }
        return result;
    }
}
