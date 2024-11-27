function solution(r1, r2) {
    let answer = 0;
    
    for (let i=1; i < r2; i++) {
         if (i < r1) {
            answer += getMaxY(i, r2, "r2") - getMaxY(i, r1, "r1");
        } else {
            answer += getMaxY(i, r2, "r2");
        }
    }
    answer *= 4;
    answer += (r2 - r1 + 1) * 4;
    return answer;
}

function getMaxY(x, r, rName) {
    const max = Math.sqrt(r * r - x * x);
    const maxToInt = parseInt(max);
    if (rName == "r1" && max - maxToInt == 0.0) {
        return maxToInt - 1;
    } else {
        return maxToInt;
    }
}