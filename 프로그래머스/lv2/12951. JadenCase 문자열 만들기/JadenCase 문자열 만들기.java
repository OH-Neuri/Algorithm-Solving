class Solution {
    public String solution(String s) {
    	StringBuilder sb = new StringBuilder();
    	
    	boolean jaden = false;
    	s = s.toLowerCase();						// 먼저 소문자로 치환
    	for (int i = 0; i < s.length(); i++) {
    		char word = s.charAt(i);
    		if (!jaden) {							// 아직 해당 단어가 jadenCase가 되지 않았을 때
    			if (word != ' ') {					// 공백 문자가 아닌 문자 중에서
    				jaden = true;
    				if (word >= 'a' && word <= 'z')	// 소문자가 들어왔다면
    					sb.append((char)(word + 'A'-'a'));	// 대문자로 바꾼다.
    				else
    					sb.append(word);			// 다른 문자면 그대로 둔다.
    			}
    			else								// 공백 문자도 그대로 둔다.
    				sb.append(word);
    		}
    		else {									// 단어가 jadenCase가 된 상태에서
    			if (word == ' ')					// 공백 문자가 들어왔다면 새로운 단어가 들어올 것이므로
    				jaden = false;					// jadenCase가 완성되지 않았음을 표시
    			sb.append(word);					// 공백 문자는 그대로 둔다.
    		}
    	}
    	
        return sb.toString();
    }
}
