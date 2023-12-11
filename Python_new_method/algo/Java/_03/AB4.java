package _03;

import java.io.*;
import java.util.StringTokenizer;

public class AB4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            try {
                StringTokenizer st = new StringTokenizer(br.readLine());
                bw.write(Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()) + "\n");
            } catch (NullPointerException e) {
                break;
            }
            bw.flush();
        }
    }
}
