function solution(s) {
    var answer = s.split(' ');
    answer.sort((a, b) => b -a);
    return answer[answer.length-1] + " " + answer[0]
}