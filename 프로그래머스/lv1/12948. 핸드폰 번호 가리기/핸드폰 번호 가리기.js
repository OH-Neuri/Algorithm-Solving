function solution(phone_number) {
 
    return ""+Array(phone_number.length-4).fill("*").join("")+phone_number.slice(phone_number.length-4,phone_number.length)+"";
}