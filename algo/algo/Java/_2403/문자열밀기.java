import java.util.*;

public class 문자열밀기 {
    public static void main(String[] args) {
        String x = "123".repeat(3);
        System.out.println(x);
        System.out.println(x.indexOf("231"));
    }

    class Solution {
        public int solution(String A, String B) {
            int ln = A.length();
            StringBuilder sb = new StringBuilder();
            for (int i=0; i<ln; i++) {
                boolean state = true;
                for (int j=0; j<ln; j++) {
                    sb.append(B.charAt((i+j)%ln));
                    if (!A.substring(0,j+1).contentEquals(sb)) {
                        state = false;
                        break;
                    }
                }
                if (state) return i;
                sb.delete(0,ln);
            }
            return -1;
        }
    }

    /*class Solution {
        public int solution(String A, String B) {
            return B.repeat(2).indexOf(A);
        }
    }*/

}
