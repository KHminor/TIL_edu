import java.io.*;
import java.util.*;

public class sw_2050 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] li = br.readLine().toCharArray();
        for (int i=0; i<li.length; i++) bw.write((int)li[i]-64+" ");
        bw.flush();
        bw.close();
    }
}
