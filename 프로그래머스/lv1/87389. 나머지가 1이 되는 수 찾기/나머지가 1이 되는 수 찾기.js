function solution(n) {
    let num =[]
    for(let i=1;i<n;i++){
        if(n%i===1) num.push(i)}
    return num[0];
}