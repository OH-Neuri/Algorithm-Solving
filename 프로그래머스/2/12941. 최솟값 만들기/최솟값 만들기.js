function solution(A,B){
    var answer = 0;
    A = A.sort((a,b)=>a-b)
    B = B.sort((a,b)=>b-a)

    return A.reduce((total, value, idx)=> total+(value*B[idx]),0)
}