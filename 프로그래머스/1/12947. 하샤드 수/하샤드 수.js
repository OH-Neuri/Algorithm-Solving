function solution(x) {
    const digits = x.toString().split('')
    
    let sum = 0;
    
    for(let digit of digits){
        sum += Number(digit)
    }
    
    if(x%sum == 0){
        return true;
    }else{
        return false;
    }
    var answer = true;

}