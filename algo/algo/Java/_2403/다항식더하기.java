import java.util.StringTokenizer;

public class 다항식더하기 {
    public static void main(String[] args) {
        System.out.println(Solution.solution("x + 10"));
    }

    protected static class Solution {
        public static String solution(String polynomial) {
            StringTokenizer st = new StringTokenizer(polynomial);
            int x = 0;
            int y = 0;
            while (st.hasMoreTokens()) {
                String s = st.nextToken();
                if (s.equals("+")) continue;
                else if (s.substring(s.length()-1).equals("x")) {
                    if (s.equals("x")) x += 1;
                    else x += Integer.parseInt(s.substring(0,s.length()-1));
                }
                else y += Integer.parseInt(s);
            }
            System.out.println(x);
            System.out.println(y);
            if (x == 0) return String.valueOf(y);
            else if (y == 0) {
                if (x == 1) return "x";
                else return x+"x";
            }
            else {
                if (x == 1) return String.format("x + %d",y);
                else return String.format("%dx + %d",x,y);
            }
        }
    }
}

