package _01;

import java.io.*;
import java.util.StringTokenizer;

public class AmB {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        StringTokenizer st = new StringTokenizer(br.readLine());
        System.out.println(Integer.parseInt(st.nextToken()) - Integer.parseInt(st.nextToken()));
    }
}
