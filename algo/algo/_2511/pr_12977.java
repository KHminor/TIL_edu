public class pr_12977 {
    public static void main(String[] args) {
        class Solution {
            public int solution(int[] nums) {
                int answer = 0;
                int ln = nums.length;
                for (int a=0; a<ln-2; a++) {
                    for (int b=a+1; b<ln-1; b++) {
                        for (int c=b+1; c<ln; c++) {
                            int now_num = nums[a]+nums[b]+nums[c];
                            boolean state = false;
                            for (int x=2; x<=(int)Math.sqrt(now_num); x++) {
                                if (now_num%x==0) {
                                    state = true;
                                    break;
                                }
                            }
                            if (!state) answer++;
                        }
                    }
                }


                return answer;
            }
        }

        class Solution2 {
            static int answer = 0;
            public int solution(int[] nums) {
                cycle(nums, 0, 0, 0);
                return answer;
            }

            public void cycle(int[] nums, int idx, int cnt, int hap) {
                if (cnt == 3) {
                    boolean state = false;
                    for (int x=2; x<=(int)Math.sqrt(hap); x++) {
                        if (hap%x==0) {
                            state=true;
                            break;
                        }
                    }
                    if (!state) answer++;
                    return;
                }
                for (int i=idx; i<nums.length; i++) {
                    cycle(nums, i+1, cnt+1, hap+nums[i]);
                }
            }
        }
    }
}
