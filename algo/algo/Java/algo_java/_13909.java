import java.util.*;

public class _13909 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int result = 1;
        int st = 3;
        int now = 1;
        while (true) {
            if (N>=now+st) {
                now+=st;
                result++;
                st+=2;
            } else break;

        }
        System.out.println(result);
    }
}

// 1    -> 1
// 2    -> 1 0
// 3    -> 1 0 0
// 4    -> 1 0 0 1
// 5    -> 1 0 0 1 0
// 6    -> 1 0 0 1 0 0
// 7    -> 1 0 0 1 0 0 0
// 8    -> 1 0 0 1 0 0 0 0
// 9    -> 1 0 0 1 0 0 0 0 1
// 10   -> 1 0 0 1 0 0 0 0 1 0
// 11   -> 1 0 0 1 0 0 0 0 1 0 0
// 12   -> 1 0 0 1 0 0 0 0 1 0 0 0
// 13   -> 1 0 0 1 0 0 0 0 1 0 0 0 0
// 14   -> 1 0 0 1 0 0 0 0 1 0 0 0 0 0
// 15   -> 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0
// 16   -> 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1

// 1 4 9 16
//  3 5 7  9

// 1 1 1 1
// 1 0 1 0
// 1 0 0 0
// 1 0 0 1


// 1 1 1 1 1
// 1 0 1 0 1
// 1 0 0 0 1
// 1 0 0 1 1
// 1 0 0 1 0


// 1 1 1 1 1 1
// 1 0 1 0 1 0
// 1 0 0 0 1 1
// 1 0 0 1 1 1
// 1 0 0 1 0 1
// 1 0 0 1 0 0

// 1 1 1 1 1 1 1
// 1 0 1 0 1 0 1
// 1 0 0 0 1 1 1
// 1 0 0 1 1 1 1
// 1 0 0 1 0 1 1
// 1 0 0 1 0 0 1
// 1 0 0 1 0 0 0



// 1 1 1 1 1 1 1 1
// 1 0 1 0 1 0 1 0
// 1 0 0 0 1 1 1 0
// 1 0 0 1 1 1 1 1
// 1 0 0 1 0 1 1 1
// 1 0 0 1 0 0 1 1
// 1 0 0 1 0 0 0 1
// 1 0 0 1 0 0 0 0


// 1 -> 16
// 2 -> 8
// 4 -> 2