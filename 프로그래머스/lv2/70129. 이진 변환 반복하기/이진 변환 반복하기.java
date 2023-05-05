import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[]{0, 0};
    while (!s.equals("1")) {
        char[] sArr = s.toCharArray();
        int temp = 0;
        for (char c : sArr) {
            if (c == '1') {
                temp++;
            }
        }
        answer[0]++;
        answer[1] += sArr.length - temp;
        s = Integer.toBinaryString(temp);
    }
    return answer;
    }
}
