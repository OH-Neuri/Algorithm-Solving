function solution(n, m, section) {
    var answer = 0;
    let idx = 1
    
    const sectionArr = Array.from({legnth : n + 1}, () => false)
    for(let s of section){
        sectionArr[s] = true
    }
    
    while(idx <= n){
        if(sectionArr[idx]){
            idx += m
            answer++;
        }else{
            idx++
        }
    }
    
    return answer;
}