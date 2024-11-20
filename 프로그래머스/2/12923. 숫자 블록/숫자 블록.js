function solution(begin, end) {
    var answer = [];
    
    // num을 넣으면 약수중에서 자신을 빼고 가장 큰 수를 리턴
    function check(num){       
        var checkArr=[];        
        if(num===1){
            return 0;
        }
        // 약수 구하기
        for(var i =2;i<=Math.sqrt(num);i++){
            if(num%i===0){
                checkArr.push(i);
                if(num/i <= 1e7){
                    return num/i;
                }
            }
        }
        if(checkArr.length!==0){
            return checkArr[checkArr.length-1];
        }     
        // 없다면 1을 리턴 (1은 모두 나눠짐.)
        return 1;
    }
    
    
    for(var i = begin;i<=end;i++){
        var checkNum = check(i);
        if(checkNum!==undefined){
             answer.push(checkNum);
        }
    }
    
    return answer;
}