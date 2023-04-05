function solution(money) {
    var answer = [];
    answer.push(~~(money/5500))
    answer.push((money%5500))
    return answer;
}