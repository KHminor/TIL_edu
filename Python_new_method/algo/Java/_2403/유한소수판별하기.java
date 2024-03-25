import java.util.*;

public class 유한소수판별하기 {
    public static void main(String[] args) {
        // 기약분수: 분자와 분모의 공약수가 1밖에 없는 것.
        // 소인수: 주어진 자연수를 나누어 떨어뜨리는 약수 중 소수(1)인 약수.

    }

    class Solution {
        public int solution(int a, int b) {
            int s = 2;
            int e = a;
            while (s <= e) {
                if (a%s==0 && b%s==0) {
                    a /= s;
                    b /= s;
                    e = a;
                } s++;
            }

            boolean state = true;
            while (true) {
                if (b%2==0) b/=2;
                else if (b%5==0) b/=5;
                else {
                    state = false;
                    break;
                }
            }

            return (b==1)?1:2;
        }
    }
}
