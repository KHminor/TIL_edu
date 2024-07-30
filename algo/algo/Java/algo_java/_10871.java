import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

//public class _10871 {
//    public static void main(String[] args) throws IOException{
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st1 = new StringTokenizer(br.readLine());
//        int n = Integer.parseInt(st1.nextToken());
//        int x = Integer.parseInt(st1.nextToken());
//        StringBuilder sb = new StringBuilder();
//        StringTokenizer st2 = new StringTokenizer(br.readLine());
//        ArrayList<Integer> li = new ArrayList<>();
//        for (int i = 0; i < n; i++) {
//            int num = Integer.parseInt(st2.nextToken());
//            if (x > num) li.add(num);
//        }
//
//        System.out.println(li.stream()
//                .map(String::valueOf)
//                .collect(Collectors.joining(" ")));
//    }
//}

public class _10871 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st1.nextToken());
        int x = Integer.parseInt(st1.nextToken());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st2.nextToken());
            if (x > num) sb.append(num).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
