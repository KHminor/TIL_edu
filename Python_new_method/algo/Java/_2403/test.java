public class test {
    public static void main(String[] args) {
        Solution.solution("3x + 7 + x");
    }
}

class Solution {
    public static String solution(String polynomial) {
        String[] li = polynomial.split(" ");
        for (String x: li) {
            System.out.println(x);
        }
        return "";
    }
}


