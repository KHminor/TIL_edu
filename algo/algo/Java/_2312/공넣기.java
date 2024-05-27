package _2312;

import java.io.*;
import java.util.*;

public class 공넣기 {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st1 = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st1.nextToken());
    int m = Integer.parseInt(st1.nextToken());
    ArrayList<Integer> li = new ArrayList<>(Collections.nCopies(n+1,0));

    for (int i = 0; i < m; i++) {
      StringTokenizer st2 = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st2.nextToken());
      int y = Integer.parseInt(st2.nextToken());
      int z = Integer.parseInt(st2.nextToken());
      for (int j = x; j <= y; j++) {
        li.set(j,z);
      }
    }
    for (int i = 1; i <= n; i++) {
      System.out.print(li.get(i) + " ");
    }
  }
}
