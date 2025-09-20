import java.io.*;
import java.util.StringTokenizer;

public class sw_2072 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        for (int i=1; i<=t; i++) {
            st = new StringTokenizer(br.readLine());
            bw.write(String.format("#%d %d",i,hol(st))+"\n");
        }
        bw.flush();
        bw.close();
    }

    public static int hol(StringTokenizer st) {
        int result = 0;
        while (st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            if (num%2!=0) result+=num;
        }
        return result;
    }
}
