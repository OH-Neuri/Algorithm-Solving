function solution(storey) {
    var answer = 0;
    var remain;
    while(storey!==0){
        remain = storey%10;
        storey = Math.floor(storey/10);

        if(remain<5){
            answer+=remain;
        }
        else if(remain>5){
            answer+=(10-remain);
            storey++;
        }
        else if(remain===5){
            answer+=5;
            if((storey%10)>=5){
                storey++;
            }
        }   
    }    
    return answer;
}