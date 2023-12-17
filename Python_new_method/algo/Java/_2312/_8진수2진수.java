package _2312;

import java.io.*;

public class _8진수2진수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine(),8);
        System.out.println(Integer.toBinaryString(num));
    }
}
