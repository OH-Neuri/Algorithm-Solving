function solution(x, y, n) {
 
    if(x===y){
        return 0;
    }else if(x>y){
        return -1;
    }
    
    let countArray = Array(y+1).fill(Infinity)
    countArray[x] = 0;
    
    for(i=x+1; i<y+1; ++i){
        if(i-n>=x){
            countArray[i] = Math.min(countArray[i],countArray[i-n]+1)
        }
        if(i%2===0&&i/2>=x){
            countArray[i] = Math.min(countArray[i],countArray[i/2]+1)         
        }
        if(i%3===0&&i/3>=x){
            countArray[i] = Math.min(countArray[i],countArray[i/3]+1)         
        }
    }
    return countArray[y]===Infinity? -1:countArray[y]
}