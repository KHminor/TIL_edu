package _2312;
import java.io.*;
import java.util.*;

public class 뒤집힌덧셈 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String x = st.nextToken();
        String y = st.nextToken();

        Integer result = Rev(x)+Rev(y);
        System.out.println(Rev(result.toString()));
    }

    public static Integer Rev(String num) {
        return Integer.parseInt(new StringBuilder(num).reverse().toString());
    }
}
