import java.util.*;
public class 특이한정렬 {
    public static void main(String[] args) {
        int[] numlist = {1,2,3,4,5,6};
        int n = 4;
        Solution solution = new Solution();
        int[] result = solution.solution(numlist,n);
        System.out.println(Arrays.toString(result));
    }

    static class Solution {
        public int[] solution(int[] numlist, int n) {
            HashMap<Integer,ArrayList<Integer>> dic = new HashMap<>();
            ArrayList<Integer> result = new ArrayList<>();
            for (int num: numlist) {
                int x = Math.abs(num-n);
                if (dic.containsKey(x)) {
                    ArrayList<Integer> li = dic.get(x);
                    li.add(num);
                }
                else {
                    ArrayList<Integer> li = new ArrayList<Integer>(Arrays.asList(num));
                    dic.put(x,li);
                }
            }

            ArrayList<Integer> s_li = new ArrayList<>(dic.keySet());
            Collections.sort(s_li);
            for (Integer key: s_li) {
                if (dic.get(key).size() != 1) {
                    Collections.sort(dic.get(key));
                    Collections.reverse(dic.get(key));
                }
                ArrayList<Integer> li = dic.get(key);
                for (Integer num: li) {
                    result.add(num);
                }

            }
            return result.stream().mapToInt(Integer::intValue).toArray();
        }
    }
}
