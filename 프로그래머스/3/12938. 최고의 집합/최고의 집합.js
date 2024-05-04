function solution(n, s) {
    if(n>s) return [-1] 
    let quotient = Math.floor(s/n)
    let remainder = s%n
    let answer = []
    
    for(let i=0;i<n;i++){
        let number = quotient
        if(remainder) {
            number +=1
            remainder-=1
        }
        answer.push(number)
    }
    answer.sort((a,b)=>a-b)
    return answer
}