function solution(arrayA, arrayB) {
    let a = getDvsr(arrayA, arrayB);
    let b = getDvsr(arrayB, arrayA);
    return Math.max(a,b);
}
function getDvsr(arrayA, arrayB){
    let answer = 0;
    const gcd =  (a, b) => a % b === 0 ? b : gcd(b, a % b);
    arrayA.forEach(val => answer = gcd(answer, val));
    if(arrayB.some(val => val%answer === 0)) return 0;
    
    return answer;
}