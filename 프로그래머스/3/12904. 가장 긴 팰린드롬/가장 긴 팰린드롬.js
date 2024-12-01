// 논리 명확하게 설정(마법수 4 넘어가지 않게)
// 문제 분석

function solution(s){
    var answer = 0;
    let len = s.length;
    
    for(let i=0;i < len; i++){
        
        //1. 홀수
        let dist = 0
        while(i - dist >= 0 && i + dist <= len){
            if(s[i-dist] == s[i+dist]){
                answer = Math.max(answer, dist*2+1)
            dist++;
                
            }else{
                break;
            }
        }
        dist = 0
        //2. 짝수
        while(i - dist >= 0 && (i+1) + dist <= len){
            if(s[i-dist] == s[(i+1) + dist]){
                answer = Math.max(answer, dist*2+2)
                dist++;
            }else{
                break;
            }
        }
    }
    return answer;
}