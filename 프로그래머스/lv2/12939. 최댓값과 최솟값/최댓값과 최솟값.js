function solution(s) {
    var answer =s.split(" ").sort((a,b)=>{
        return a-b;
    })
    var arr = [];
    arr.push(answer[0])
    arr.push(answer[answer.length-1])
    return arr.join(" ");
}