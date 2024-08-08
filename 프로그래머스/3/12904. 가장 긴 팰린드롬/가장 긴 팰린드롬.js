function solution(s){
    var answer = 1;
    
    for(let i=0; i<s.length; i++){
        // 바로 앞 검사
        if(s[i] && s[i+1] && s[i] == s[i+1]){
            let sIdx = i
            let eIdx = i+1
            while(s[sIdx] && s[eIdx] && s[sIdx] == s[eIdx]){
                sIdx -=1
                eIdx +=1
                answer = Math.max(answer, (eIdx-sIdx-1))
            }
        }
        // 양옆 검사
        if(s[i-1] && s[i+1] && s[i-1] == s[i+1]){
            let sIdx = i-1
            let eIdx = i+1
            while(s[sIdx] && s[eIdx] &&  s[sIdx] == s[eIdx]){
                sIdx -=1
                eIdx +=1
                answer = Math.max(answer, (eIdx-sIdx-1))
            }
        }
    }
    
    return answer;
}