import java.util.*;
import java.util.stream.Collectors;

public class _pro_84512 {
    public static void main(String[] args) {

    }

    class Solution {
        static List<String> li;
        static String[] words = {"A","E","I","O","U"};

        public int solution(String word) {
            li = new ArrayList<>();
            find("",0);
            for (int i=0; i<li.size(); i++) {
                if (word.equals(li.get(i))) return i;
            }
            return 0;
        }

        static void find(String str, int len) {
            li.add(str);
            if (len==5) return;
            for (int i=0; i<5; i++) find(str+words[i],len+1);
        }
    }

    class Solution2 {
        static Deque<String> li;
        static String[] words = {"A","E","I","O","U"};
        static int cnt = 0;
        public int solution(String word) {
            li = new ArrayDeque<>();
            return find(word);
        }

        static int find(String word) {
            if ((word.length()==li.size())
                    &&(li.stream().map(String::valueOf).collect(Collectors.joining("")).equals(word))) return cnt;
            else if (li.size()==5) return -1;
            for (String w: words) {
                li.add(w);
                cnt++;
                int check = find(word);
                if (check != -1) return check;
                li.pollLast();
            }
            return -1;
        }

    }
}

