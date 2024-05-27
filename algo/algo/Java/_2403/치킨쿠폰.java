public class 치킨쿠폰 {
    class Solution {
        class x {
            public int solution(int chicken) {
                int result = chicken/9;
                if (chicken > 1 && chicken%9==0) result--;
                return result;
            }
        }
    }
}
