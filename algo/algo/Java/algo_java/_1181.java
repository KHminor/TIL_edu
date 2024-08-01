import java.io.*;
import java.util.*;
public class _1181 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        int n = Integer.parseInt(br.readLine());
//        int mx_ln = 0;
//        List<String> li = new ArrayList<>(n);
//        int[] check_li = new int[51];
//
//        for (int i=0; i<n; i++) {
//            String inp = br.readLine();
//            int inp_ln = inp.length();
//            if (!li.contains(inp)) {
//                 li.add(inp);
//                mx_ln = Math.max(mx_ln, inp_ln);
//                 check_li[inp_ln]++;
//            }
//        }
//
//        br.close();
//
//        List<List<String>> mtrix = new ArrayList(mx_ln+1);
//
//        for (int i=0; i<=mx_ln; i++) mtrix.add(new ArrayList<>(check_li[i]));
//
//        for (String inp: li) mtrix.get(inp.length()).add(inp);
//
//        for (List<String> i: mtrix) {
//            Collections.sort(i);
//            for (String j: i) bw.write(j+"\n");
//        }
//
//        bw.flush();
//        bw.close();
//    }


//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        int n = Integer.parseInt(br.readLine());
//
//        String[] arr = new String[n];
//
//        for (int i=0; i<n; i++) arr[i] = br.readLine();
//
//        Arrays.sort(arr, new Comparator<String>() {
//            public int compare(String s1, String s2) {
//                if (s1.length() == s2.length()) return s1.compareTo(s2);
//                else return s1.length() - s2.length();
//            }
//        });
//
//        System.out.println(Arrays.toString(arr));
//    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        List<String> arr = new ArrayList<>(n);
        for (int i=0; i<n; i++) {
            String next_st = br.readLine();
            if (!arr.contains(next_st)) arr.add(next_st);
        }

        Collections.sort(arr, new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (s1.length() == s2.length()) return s1.compareTo(s2);
                else return s1.length() - s2.length();
            }
        });

        for (String i: arr) {
            bw.write(i+"\n");
        }

        bw.flush();
        bw.close();
    }
}
