import java.io.*;
import java.util.*;

public class _9184 {
    private static Map<String, Integer> dic = new HashMap<>();
//    private static int[][][] mtx = new int[21][21][21];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (a == -1 && a == b && a == c) break;
            bw.write(String.format("w(%d, %d, %d) = %d", a, b, c, rec(a, b, c)) + "\n");
        }
        bw.flush();
    }

    public static int rec(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) return 1;
        else if (a > 20 || b > 20 || c > 20) {
            int r1;
            if (dic.containsKey("202020")) r1 = dic.get("202020");
            else {
                dic.put("202020", rec(20,20,20));
                r1 = dic.get("202020");
            }
            return r1;
        }
        else if (a < b && b < c) {
            int r1;
            int r2;
            int r3;
            if (dic.containsKey(s_change(a,b,c-1))) r1 = dic.get(s_change(a,b,c-1));
            else {
                dic.put(s_change(a,b,c-1), rec(a,b,c-1));
                r1 = dic.get(s_change(a,b,c-1));
            }
            if (dic.containsKey(s_change(a,b-1,c-1))) r2 = dic.get(s_change(a,b-1,c-1));
            else {
                dic.put(s_change(a,b-1,c-1), rec(a,b-1,c-1));
                r2 = dic.get(s_change(a,b-1,c-1));
            }
            if (dic.containsKey(s_change(a,b-1,c))) r3 = dic.get(s_change(a,b-1,c));
            else {
                dic.put(s_change(a,b-1,c), rec(a,b-1,c));
                r3 = dic.get(s_change(a,b-1,c));
            }
            return r1 + r2 - r3;
        } else {
            int r1;
            int r2;
            int r3;
            int r4;
            if (dic.containsKey(s_change(a-1,b,c))) r1 = dic.get(s_change(a-1,b,c));
            else {
                dic.put(s_change(a-1,b,c), rec(a-1,b,c));
                r1 = dic.get(s_change(a-1,b,c));
            }
            if (dic.containsKey(s_change(a-1,b-1,c))) r2 = dic.get(s_change(a-1,b-1,c));
            else {
                dic.put(s_change(a-1,b-1,c), rec(a-1,b-1,c));
                r2 = dic.get(s_change(a-1,b-1,c));
            }
            if (dic.containsKey(s_change(a-1,b,c-1))) r3 = dic.get(s_change(a-1,b,c-1));
            else {
                dic.put(s_change(a-1,b,c-1), rec(a-1,b,c-1));
                r3 = dic.get(s_change(a-1,b,c-1));
            }
            if (dic.containsKey(s_change(a-1,b-1,c-1))) r4 = dic.get(s_change(a-1,b-1,c-1));
            else {
                dic.put(s_change(a-1,b-1,c-1), rec(a-1,b-1,c-1));
                r4 = dic.get(s_change(a-1,b-1,c-1));
            }
            return r1 + r2 + r3 - r4;
        }
    }

//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        StringTokenizer st;
//
//        while (true) {
//            st = new StringTokenizer(br.readLine());
//            int a = Integer.parseInt(st.nextToken());
//            int b = Integer.parseInt(st.nextToken());
//            int c = Integer.parseInt(st.nextToken());
//            if (a == -1 && a == b && a == c) break;
//            bw.write(String.format("w(%d, %d, %d) = %d", a, b, c, rec(a, b, c)) + "\n");
//        }
//        bw.flush();
//    }
//
//    public static int rec(int a, int b, int c) {
//        if (check(a,b,c)&&mtx[a][b][c]!=0) return mtx[a][b][c];
//        else if (a<=0 || b<=0 || c<=0) return 1;
//        else if (a>20 || b>20 || c>20) return mtx[20][20][20]=rec(20, 20, 20);
//        else if (a<b&&b<c) return mtx[a][b][c]=rec(a,b,c-1)+rec(a,b-1,c-1)-rec(a,b-1,c);
//        else return mtx[a][b][c]=rec(a-1,b,c)+rec(a-1,b-1,c)+rec(a-1,b,c-1)-rec(a-1,b-1,c-1);
//    }
//
//    public static boolean check(int a, int b, int c) {
//        return 0 <= a && a <= 20 && 0 <= b && b <= 20 && 0 <= c && c <= 20;
//    }

    public static String s_change(int a, int b, int c) {
        String s_a = 10>a?"0"+a:String.valueOf(a);
        String s_b = 10>b?"0"+b:String.valueOf(b);
        String s_c = 10>c?"0"+c:String.valueOf(c);
        return s_a+s_b+s_c;
    }
}

