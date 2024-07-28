function solution(s) {
    var answer = s.split(" ").map(Number)
    return Math.min(...answer)+ " "+Math.max(...answer);
}