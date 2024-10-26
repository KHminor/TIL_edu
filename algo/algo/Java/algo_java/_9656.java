import java.util.Scanner;
public class _9656 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] result = {"SK","CY"};
        if (N%3==0) System.out.println(result[(N/3)%2]);
        else System.out.println(result[(N/3+N%3)%2]);
    }
}
