import java.util.*;
class Solution {
    public  int[] solution(int n, long left, long right) {
        // 딱 필요한 만큼만 저장할 배열 만들기
        int[] answer = new int[(int)(right - left) + 1];
        
        // 규칙 찾기
        // 인덱스 : 1 2 3 4 5 6 7 8 9 ...
        // 값    : 1 2 3 4 2 2 3 4 3 3 3 4 4 ...
        // 해당 인덱스와 n값을 나누거나, 나머지 연산한 결과 중 큰 수에다가 +1를 저장한다.
        for (int i = 0; i < answer.length; i++) {
            int max = Math.max((int)((left + i) / n), (int)((left + i) % n));
            answer[i] = max + 1;
        }
        
        return answer;
    }
}