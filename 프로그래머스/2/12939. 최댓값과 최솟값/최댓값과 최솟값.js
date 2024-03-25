function solution(s) {
    var answer = s.split(' ').map(i=>Number(i))
    return Math.min.apply(null,answer)+" "+ Math.max.apply(null,answer);
}
