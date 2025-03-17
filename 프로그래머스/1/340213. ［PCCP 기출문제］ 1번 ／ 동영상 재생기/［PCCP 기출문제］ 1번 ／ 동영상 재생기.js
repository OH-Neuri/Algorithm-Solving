function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';
    let videoSeconds = timeToSeconds(video_len) // 동영상 길이
    let opStartSeconds = timeToSeconds(op_start) // 오프닝 시작 시각
    let opEndSeconds = timeToSeconds(op_end) // 오프닝 끝나는 시각
    let currentSeconds = timeToSeconds(pos) // 현재 재생 위치

    for(let [command] of commands){
        // 오프닝체크
        if(opStartSeconds<=currentSeconds 
           && currentSeconds<=opEndSeconds) currentSeconds = opEndSeconds;
        
        // 이전
        if(command==="p"){
            currentSeconds = currentSeconds - 10 >=0 ? currentSeconds - 10 : 0
        }else{
        // 다음
            currentSeconds = currentSeconds + 10 <= videoSeconds ? currentSeconds + 10 : videoSeconds
        }
        
        // 오프닝체크
        if(opStartSeconds<=currentSeconds 
           && currentSeconds<=opEndSeconds) currentSeconds = opEndSeconds;
    }
    
    const mm = Math.floor(currentSeconds/60);
    const ss = currentSeconds % 60;
    const result = `${String(mm).padStart(2,'0')}:${String(ss).padStart(2,'0')}`
    return result;
}

function timeToSeconds(time){
    const [mm, ss] = time.split(":").map(Number);
    return mm * 60 + ss;
}


