function solution(A, B) {
    var answer = 0;
    A = A.sort((a,b)=>a-b)
    B = B.sort((a,b)=>a-b)
    
    let idx = 0
    for(let i = 0; i < B.length; i++){
        if(A[idx] < B[i]) {
            answer++; 
            idx++;
        }
    }
    return answer;
}