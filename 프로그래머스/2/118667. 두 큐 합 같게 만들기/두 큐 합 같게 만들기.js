function solution(queue1, queue2) {
    var answer = 0;
    var queueSum1 = 0;
    queue1.forEach(element=>queueSum1+=element);
    var queueSum2 = 0;
    queue2.forEach(element=>queueSum2+=element);
    var totalLen = queue1.length+ queue2.length;
    var queue1Index = 0;
    var queue2Index = 0;
    
    while(queueSum1 !== queueSum2){
        if(queueSum1>queueSum2){
            queueSum1 -= queue1[queue1Index];
            queue2.push(queue1[queue1Index]);
            queueSum2 +=queue1[queue1Index++];
        }
        else{
             queueSum1 += queue2[queue2Index];
             queue1.push(queue2[queue2Index]);
             queueSum2 -=queue2[queue2Index++];
        }
         answer++;
        if(queue1Index>totalLen||queue2Index>totalLen){
            return -1;
        }
    }
    return answer;
}