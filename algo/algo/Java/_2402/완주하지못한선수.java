import java.util.HashMap;

public class 완주하지못한선수 {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        System.out.println(s.solution(participant,completion));
    }
}

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String,Integer> hm = new HashMap<>();
        String result = "";
        for (String i: participant) {
            if (hm.containsKey(i)) hm.put(i,hm.get(i)+1);
            else hm.put(i,1);
        }
        for (String i: completion) hm.put(i,hm.get(i)-1);
        for (String i: hm.keySet()) {
            if (hm.get(i) != 0) {
                result = i;
                break;
            };
        }
        return result;
    }
}
