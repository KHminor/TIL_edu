import java.util.*;
import java.util.stream.Collectors;

public class _test {
    public static void main(String[] args) {
        int[][] li = {
                {3, 2},
                {1, 5},
                {3, 1},
                {2, 4},
                {1, 2}
        };

        Arrays.sort(li, new Comparator<int[]>() {
            public int compare(int[] a1, int[] a2) {
                if (a1[0]!=a2[0]) return a1[0]-a2[0];
                else return a2[1]-a1[1];
            }
        });
        for (int[] x: li) System.out.println(Arrays.toString(x));
    }
}
