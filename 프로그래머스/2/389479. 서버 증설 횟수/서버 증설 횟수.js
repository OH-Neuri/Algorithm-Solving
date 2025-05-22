function solution(players, m, k) {
    const nSMap = new Map()
    let nSId = 0
    
    for(let time = 0; time < players.length; time++){
        
        // 가동중인 서버 진행 시간 갱신 및 종료 
        if(nSMap.size > 0){
            
            for(let [key, value] of nSMap){
                const nowTime = value + 1;
                if(nowTime > k) {
                    nSMap.delete(key)
                }else { 
                    nSMap.set(key, nowTime)
                }
            }
        }
        
        // 서버 증설
        if(players[time] / m > nSMap.size){
            const addServer = Math.floor(players[time] / m) - nSMap.size
            
            for(let i = 0; i < addServer; i++){
                nSMap.set(nSId++, 1)
            }
        }
    }
    
    return nSId;
}