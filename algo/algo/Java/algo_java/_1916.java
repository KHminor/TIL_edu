import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class _1916 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        long[] check = IntStream.rangeClosed(0,N).mapToLong(i->1000000000L).toArray();
        Deque<List<Long>> dq = new ArrayDeque<>();
        List<List<List<Integer>>> arr = new ArrayList<>();
        for (int i=0; i<=N; i++) arr.add(new ArrayList<>());
        StringTokenizer st;
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            arr.get(idx).add(new ArrayList<>(Arrays.asList(idx,Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()))));
        }
        st = new StringTokenizer(br.readLine());
        long start = Long.parseLong(st.nextToken());
        long end = Long.parseLong(st.nextToken());
        dq.add(new ArrayList<>(Arrays.asList(start,0L)));

        long result = 1000000000L;
        // bfs
        while (!dq.isEmpty()) {
            System.out.println(dq);
            List<Long> now = dq.pollFirst();
            if (now.get(1)>=result) continue;

            if (now.get(0)==end && result>now.get(1)) result = now.get(1);
            else {
                for (List<Integer> li: arr.get(Math.toIntExact(now.get(0)))) {
                    if (result>now.get(1)+li.get(2) && check[Math.toIntExact(now.get(0))]>now.get(1)+li.get(2)) {
                        dq.add(new ArrayList<>(Arrays.asList((long)li.get(1),now.get(1)+li.get(2))));
                        check[Math.toIntExact(now.get(0))] = now.get(1)+li.get(2);
                    }
                }
            }
        }
        System.out.println(result);
    }
}

//4
//5
//1 2 10
//1 4 5
//4 2 1
//2 3 1
//4 3 10
//1 3