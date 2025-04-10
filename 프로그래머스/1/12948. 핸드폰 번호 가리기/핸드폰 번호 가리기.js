function solution(phone_number) {
    const len = phone_number.length
    var answer = "*".repeat(len-4)
    for(let i = len - 4 ; i < len; i++){
        answer += phone_number[i]
    }
    return answer
}