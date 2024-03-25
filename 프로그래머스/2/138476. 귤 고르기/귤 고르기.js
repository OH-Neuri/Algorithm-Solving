function solution(k, tangerine) {
    var answer = 0;
    let hash = {}
    tangerine.forEach(t=>{
        if(hash[t]==undefined) { hash[t] =1 }
        else {hash[t] +=1}
    })
    let sortedKeys = Object.keys(hash).sort((a, b) => hash[b] - hash[a]);
    
    for(let i=0;i<sortedKeys.length;i++){
        k-=hash[sortedKeys[i]]
        answer+=1
        if(k<=0) break;
    }
    return answer;
}