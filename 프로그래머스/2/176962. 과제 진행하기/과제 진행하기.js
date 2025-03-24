function solution(plans) {
    var answer = [];
    let stack = [];
    const pLen = plans.length
    plans.sort((a,b)=> convertToMinutes(a[1]) - convertToMinutes(b[1]))
    
    for(let i = 0; i < pLen- 1; i++){
        const [name, startTime, duration] = plans[i];
        const currentStart = convertToMinutes(startTime);
        const currentDuration = Number(duration);
        const nextStart = convertToMinutes(plans[i+1][1])
        let remainTime = nextStart - (currentStart + currentDuration) // 여유 시간
        
        
        if(remainTime >= 0){
            // 현재 과제 완료
            answer.push(name)
            
            // 여유 시간으로 이전 과제 진행
            while(remainTime > 0 && stack.length>0){
                const [prevName, prevRemain] = stack.pop();
                
                if(remainTime >= prevRemain){
                    remainTime -= prevRemain
                    answer.push(prevName)
                }else{
                    stack.push([prevName, prevRemain - remainTime])
                    break;
                }
            }
        }else{                     
            stack.push([name, -remainTime]) // 남은 과제 시간 push
        }
    }
    
    // 마지막 과제는 무조건 끝남
    answer.push(plans[pLen-1][0])
    
    while(stack.length>0){
        answer.push(stack.pop()[0])
    }
    
    return answer;
}

// "mm:ss" 형식을 분으로 변환하는 함수
function convertToMinutes(timeStr){
    let [hh, mm] = timeStr.split(":").map(Number)
    return hh*60 + mm
}