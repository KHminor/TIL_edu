import java.io.*;
import java.util.*;
public class _1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[] pokemon = new String[N];
        Map<String, Integer> dic = new HashMap<>(N);
        for (int i=0; i<N; i++) {
            String poke = br.readLine();
            pokemon[i] = poke;
            dic.put(poke,i+1);
        }
        while (M>0) {
            String inp = br.readLine();
            if (Character.isDigit(inp.charAt(0))) bw.write(pokemon[Integer.parseInt(inp)-1]+"\n");
            else bw.write(dic.get(inp)+"\n");
            M--;
        }
        bw.flush();
    }

    public static boolean isNum(String str) {
        return str.matches("-?\\d+(\\.\\d+)?");
    }
//    public static boolean isStr(String str) {
//        return str.matches("^[0-9]+$");
//    }
}
