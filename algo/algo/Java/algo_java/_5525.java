import java.io.*;
public class _5525 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        String s = br.readLine();
        System.out.println(findResult(M,N*2+1,s));
    }
//    private static String makeString(int N) {
//        StringBuilder sb = new StringBuilder();
//        for (int i=0; i<N; i++) sb.append("IO");
//        sb.append("I");
//        return sb.toString();
//    }

//    private static int findResult(int M, int ms_ln, String ms, String s) {
//        int cnt = 0;
//        for (int i=0; i<=M-ms_ln; i++) {
//            if (s.substring(i,i+ms_ln).equals(ms)) cnt++;
//        }
//        return cnt;
//    }

    private static int findResult(int M, int ms_ln, String s) {
        int cnt = 0;
        int ln = 0;
        char[] check = {'I','O'};
        for (int i=0; i<M; i++) {
            if (check[ln%2]==s.charAt(i)) ln++;
            else {
                cnt+=cal(ms_ln, ln);
                ln=check[0]==s.charAt(i)?1:0;
            }
        }
        if (ln!=0) cnt+=cal(ms_ln, ln);
        return cnt;
    }

    private static int cal(int ms_ln, int ln) {
        return ln>=ms_ln?(ln-ms_ln)/2+1:0;
    }
}

// 7
//
// 7-5=2 ->  0,2
// 7-3=4 ->  0,2,4
// 8-3=5 ->  0,2,4
// 9-3=6 ->  0,2,4,6