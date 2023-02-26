function solution(n) {
    var nArr = (n+"").split("");
    var answer =[];
    for(let i=nArr.length-1;i>=0;i--){
        answer.push(Number(nArr[i]));
    }
    return answer;
}