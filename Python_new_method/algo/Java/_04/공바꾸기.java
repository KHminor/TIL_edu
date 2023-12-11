package _04;

        import java.io.*;
        import java.util.*;

public class 공바꾸기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        LinkedList<Integer> li = new LinkedList<>();

        for (int i = 0; i <= n; i++) {
            li.add(i);
        }


        for (int i = 0; i < m; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st2.nextToken());
            int y = Integer.parseInt(st2.nextToken());

            int xNum = li.get(x);
            int yNum = li.get(y);

            li.set(x,yNum);
            li.set(y,xNum);
        }

        for (int i = 1; i <= n; i++) {
            System.out.print(li.get(i) + " ");
        }
        System.out.println();
    }
}
