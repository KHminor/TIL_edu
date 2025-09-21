import java.io.*;
import java.util.*;
import java.util.stream.Stream;

public class sw_2056 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Map<String, Integer> dic = new HashMap<String, Integer>() {{
            put("01", 31);
            put("02", 28);
            put("03", 31);
            put("04", 30);
            put("05", 31);
            put("06", 30);
            put("07", 31);
            put("08", 31);
            put("09", 30);
            put("10", 31);
            put("11", 30);
            put("12", 31);
        }};

        int t = Integer.parseInt(br.readLine());
        for (int i=1; i<=t; i++) {
            String fullYear = br.readLine();
            bw.write(String.format("#%d %s", i, research(fullYear.substring(0,4), fullYear.substring(4,6), fullYear.substring(6,8), dic))+"\n");
        }
        bw.flush();
        bw.close();

    }

    public static String research(String year, String month, String day, Map<String, Integer> dic) {
        String result = "-1";
        int i_month = Integer.parseInt(month);
        int i_day = Integer.parseInt(day);
        if (0<i_month && i_month<=12) {
            if (0<i_day && i_day <= dic.get(month)) {
                return String.format("%s/%s/%s", year, month, day);
            } else return result;
        } else return result;
    }
}
