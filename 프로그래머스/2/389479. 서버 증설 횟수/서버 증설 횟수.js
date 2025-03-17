function solution(players, m, k) {
    var answer = 0;
    const queue = []
    
    for(let time = 0; time <24; time++){
        // 현재 시간대에 필요한 서버 수 
        const currServer = Math.floor(players[time]/m)
        
        let i = 0;
        while (i < queue.length) {
            queue[i] -= 1;
            if (queue[i] === 0) {
                queue.splice(i, 1);  // 현재 요소 제거
            } else {
                i++;  // 제거되지 않은 경우에만 다음 인덱스로 이동
            }
        }
       
        // 현재 증설해야하는 서버 수 
        const rqServer = currServer-queue.length
        if(queue.length < currServer){
            for(let j=0;j<rqServer; j++){
                queue.push([k])
                answer++;
            }
        }
    }
    return answer;
}