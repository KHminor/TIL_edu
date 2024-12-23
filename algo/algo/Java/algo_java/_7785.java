import java.io.*;
import java.util.*;

public class _7785 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        StringTokenizer st;
//        int N = Integer.parseInt(br.readLine());
//        Map<String, String> dic = new HashMap<>();
//        for (int i=0; i<N; i++) {
//            st = new StringTokenizer(br.readLine());
//            String k = st.nextToken();
//            String v = st.nextToken();
//            dic.put(k,v);
//        }
//        List<String> result = new ArrayList<>();
//        List<String> dic_li = new ArrayList<>(dic.keySet());
//        Collections.sort(dic_li);
//        for (int i=0; i<dic_li.size(); i++) {
//            if (dic.get(dic_li.get(i)).equals("enter")) result.add(dic_li.get(i));
//        }
//        Collections.reverse(result);
//        for (String name: result) bw.write(name+"\n");
//        bw.flush();
//    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        Set<String> s_li = new HashSet<>();
        while (N>0) {
            st = new StringTokenizer(br.readLine());
            String nm = st.nextToken();
            String cmd = st.nextToken();
            if (cmd.equals("enter")) s_li.add(nm);
            else s_li.remove(nm);
            N--;
        }
        List<String> result = new ArrayList<>(s_li);
        Collections.sort(result, Collections.reverseOrder());
        for (String name: result) bw.write(name+"\n");
        bw.flush();
    }
}
