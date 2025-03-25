function solution(s, skip, index) {
    var answer = '';
    
    
    for(let char of s){
        let count = 0;
        let code = char.charCodeAt(0); 
        
        while(count < index){
            code++;
            if(code > 'z'.charCodeAt(0)) code = 97 // 'a'
            
            const nextChar = String.fromCharCode(code);
            if(!skip.includes(nextChar)) count++;
        }
        answer += String.fromCharCode(code)
    }
    
    return answer;
}