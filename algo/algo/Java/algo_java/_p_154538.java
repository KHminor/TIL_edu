import java.util.*;
public class _p_154538 {
    public static void main(String[] args) {

    }

    public static int s1(int x, int y, int n) {
        Queue<int[]> li = new LinkedList<>() {{
            add(new int[]{x,0});
        }};
        Set<Integer> visit = new HashSet<>() {{
            add(x);
        }};
        while (!li.isEmpty()) {
            int[] now = li.poll();
            if (now[0] == y) return now[1];
            for (int num: new int[]{now[0]+n,now[0]*2,now[0]*3}) {
                if (num<=y && !visit.contains(num)) {
                    visit.add(num);
                    li.add(new int[]{num,now[1]+1});
                }
            }
        }
        return -1;
    }

    public static int s2(int x, int y, int n) {
        int[] dp = new int[y+1];
        for (int i=x; i<=y; i++) {
            if (i!=x && dp[i]==0) {
                dp[i]=-1;
                continue;
            }

            if (i+n<=y) dp[i+n] = (dp[i+n]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i+n]);
            if (i*2<=y) dp[i*2] = (dp[i*2]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i*2]);
            if (i*3<=y) dp[i*3] = (dp[i*3]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i*3]);
        }
        return dp[y];
    }
}
