import java.util.Arrays;

public class 캐릭터의좌표 {
    public static void main(String[] args) {
        캐릭터좌표 c = new 캐릭터좌표();
        System.out.println(Arrays.toString(c.solution(new String[]{"left", "right", "up", "right", "right"}, new int[]{11, 11})));
    }


}


class 캐릭터좌표 {
    public int[] solution(String[] keyinput, int[] board) {
        int[] mx = new int[]{board[0]/2,board[1]/2};
        int[] answer = new int[]{0,0};

        for (String key: keyinput) {
            if (key.equals("right") && mx[0] >= answer[0]+1) answer[0] += 1;
            else if (key.equals("left") && mx[0] >= Math.abs(answer[0]-1)) answer[0] -= 1;
            else if (key.equals("up") && mx[1] >= answer[1]+1) answer[1] += 1;
            else if (key.equals("down") && mx[1] >= Math.abs(answer[1]-1)) answer[1] -= 1;
        }
        return answer;
    }
}