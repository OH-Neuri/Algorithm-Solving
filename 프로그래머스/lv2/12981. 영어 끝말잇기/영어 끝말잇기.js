function solution(n, words) {
    let answer = [0,0]
    
    for(let i=0;i<words.length;i++){
        let word = words[i]
        let p = i%n+1;
        let turn = Math.ceil((i+1)/n)
        
        if(i>0){
            let last = words[i-1].split("").pop();
            
            //중복이거나 틀린경우
            if(i>words.indexOf(word)||last!==words[i][0]){
                answer = [p,turn];
                break;
            }
        }
    }
    return answer                            
}