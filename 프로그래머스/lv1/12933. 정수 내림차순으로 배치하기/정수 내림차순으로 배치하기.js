function solution(n) {
    return Number((n+"").split("").sort().reverse().join(''));
}