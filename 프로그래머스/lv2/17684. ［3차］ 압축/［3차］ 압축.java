import java.util.*;

class Solution {
    Map<String, Integer> map = new HashMap<>();
    List<Integer> answerList = new ArrayList<>();

    public int[] solution(String msg) {
        int[] answer = {};
        int index = 0;
        // 사전 초기화
        initMap();
        String w = ""; // 현재입력
        String c = ""; // 다음글자
        int num = 0; // 압축번호
        
        for (int i = 0; i < msg.length(); i++) {
            w += msg.charAt(i); // 현재 글자
            num = cal(w); // 해당 단어 색인번호 추출, num에 저장
            if (i + 1 < msg.length()) { // 뒤에 문자남은 경우
                c = "" + msg.charAt(i + 1); // 뒤에 남은 문자 c에 저장
                String wc = w + c;
                if (cal(wc) != -1) { // w+c 가 사전에 있는 경우 넘어감
                    continue;
                }
                w = wc; // 사전추가(w+c) 만들어줌
            }
            answerList.add(num); // 현재 w의 색인 번호 저장, 
            addMap(w); // 색인번호 추가
            w = ""; //초기화
        }
        answer = new int[answerList.size()];
        for (int i=0; i<answer.length; i++){
            answer[i] = answerList.get(i);
        }
        return answer;
    }

    // map 초기화
    private void initMap() {
        char c = 'A';
        for (int i = 1; i <= 26; i++) {
            map.put(c + "", i);
            c++;
        }
    }

    // 해당 단어 색인번호 추출
    private int cal(String str) {
        int num = -1;
        if (map.containsKey(str)) {
            num = map.get(str);
        }
        return num;
    }

    // 사전추가
    private void addMap(String str) {
        map.put(str, map.size() + 1);
    }

}