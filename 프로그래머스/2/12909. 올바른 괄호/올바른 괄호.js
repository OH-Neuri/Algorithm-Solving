function solution(s){
    let sum = 0
    for(t of s){
        sum += t ==="("? 1: -1
        if(sum<0){
            return false
        }
    }

    return sum==0?true:false;
}