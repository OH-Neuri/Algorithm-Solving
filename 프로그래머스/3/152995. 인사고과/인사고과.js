function solution(scores) {
    var answer = 1;
    let wh = scores[0]
    let sortedScores = scores.sort((a,b)=>{if(a[0]===b[0]){return a[1]-b[1]}else{return b[0]-a[0]}})
    let maxVal = 0
    for (let [a,b] of sortedScores){
        if(a > wh[0] && b > wh[1]) return -1;
        if(b>=maxVal){
            if(a+b > wh[0] + wh[1]) answer ++;
            maxVal = b
        }
    }
    return answer;
}