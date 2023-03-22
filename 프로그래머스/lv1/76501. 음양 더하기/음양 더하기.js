function solution(absolutes, signs) {
    var answer = 0;
    return ((absolutes.map((v,i)=>signs[i]?answer+v:answer-v)).reduce((sum,i)=>sum+i,0))
}