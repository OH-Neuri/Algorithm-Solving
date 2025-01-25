function solution(clothes) {
    var answer = 1;
    let cMap = new Map();
    
    for(let [c, k] of clothes) {
        if(cMap.has(k)) cMap.set(k, cMap.get(k) + 1);
        else cMap.set(k, 1);
    }
    
    for(let i of cMap.values()) {
        answer *= (i+1)
    }
    
    answer -= 1;
    return answer;
}