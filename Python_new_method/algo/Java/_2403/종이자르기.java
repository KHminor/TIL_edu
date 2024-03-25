import java.util.stream.*;

public class 종이자르기 {
    public static void main(String[] args) {
        int n = 123;
        int result = 0;
        String s_n = String.valueOf(n);
        for (int idx: IntStream.range(0,s_n.length()).toArray()) result += Integer.parseInt(String.valueOf(s_n.charAt(idx)));
        System.out.println(result);
    }

}
