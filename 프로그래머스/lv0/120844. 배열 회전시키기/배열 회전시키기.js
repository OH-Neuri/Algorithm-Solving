function solution(numbers, direction) {
    if(direction=="right"){
        let last = numbers[numbers.length-1]
        numbers = numbers.map((v,i)=>numbers[i-1])
        numbers[0] = last;
    }else{
        let last = numbers[0]
        numbers = numbers.map((v,i)=>numbers[i+1])
        numbers[numbers.length-1] = last;
    }
    return numbers;
}