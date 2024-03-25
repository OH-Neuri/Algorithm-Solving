function solution(phone_number){
    const backNumber = phone_number.split('').splice(-4);
    let answer ='*'.repeat(phone_number.length-backNumber.length) + backNumber.join('')
    return answer;
}