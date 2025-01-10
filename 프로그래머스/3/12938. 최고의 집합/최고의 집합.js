function solution(n, s) {
    if(n>s) return [-1];
    var answer = [];
    
    let first = Math.floor(s/n)
    for(let i=0;i<n;i++){
        answer.push(first)
    }
    
    let idx = 0
    let second = s%n
    
    while(second!==0){
        answer[idx] +=1
        second--;
        idx++;
    }
    
    return answer.sort();
}