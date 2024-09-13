import java.io.*;
import java.util.*;
import java.util.stream.*;

public class _25325 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Map<String,Integer> dic = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        String[] s_li = new String[n];
        int[] result = new int[n];
        int cnt = 0;
        while (st.hasMoreTokens()) {
            s_li[cnt] = st.nextToken();
            cnt++;
        }
        Arrays.sort(s_li);
        for (int i=0; i<n; i++) dic.put(s_li[i],i);


        int mx = 0;
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int idx = dic.get(st.nextToken());
                result[idx]++;
                mx = Math.max(result[idx],mx);
            }
        }

//        System.out.println(Arrays.toString(result));

        // 이제 result 의 값을 기준으로 list를 다시 만들기?
        List<List<String>> r_result = IntStream.rangeClosed(0,mx).mapToObj(ArrayList<String>::new).collect(Collectors.toList());

        for (int i=0; i<n; i++) r_result.get(result[i]).add(s_li[i]);

        for (int i=mx;i>=0; i--) {
            for (String student: r_result.get(i)) bw.write(String.format("%s %d",student,i)+"\n");
        }
        bw.flush();
    }
}

