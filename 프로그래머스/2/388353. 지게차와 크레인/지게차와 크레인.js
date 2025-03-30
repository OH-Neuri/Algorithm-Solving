function solution(storage, requests) {
    var answer = 0;
    const strR = storage.length
    const strC = storage[0].length
    const outR = strR + 2
    const outC = strC + 2
    const outerMap = Array.from({length : outR}, ()=> Array.from({length : outC}, () => ""))
    const dir = [[0,1], [0,-1], [1, 0], [-1,0]]
    
    for(let i = 1; i <= strR; i++){
        for(let j = 1; j <= strC; j++){
            outerMap[i][j] = storage[i-1][j-1]
        }
    }
    // requests -> 
      // 명령1. BFS
      // 명령2. 반복문 빵꾸
    for(let request of requests){
        if(request.length===1){
            BFS(request)
        }else{
            for(let i = 0; i < outR; i++){
                for(let j = 0; j < outC; j++){
                    if(outerMap[i][j] === request[0]) outerMap[i][j] = ""
                }
            }
        }
    }
    
    function BFS(request){
        const visited = Array.from({length : outR}, ()=> Array.from({length : outC}, () => false))
        const queue = []
        queue.push([0,0])
        visited[0][0] = true
        let begin = 0
        while(begin < queue.length){
            const [cy, cx] = queue[begin++]
            for(let k = 0; k < 4; k++){
                const ny = cy + dir[k][0]
                const nx = cx + dir[k][1]
                
                if(ny < 0 || ny >= outR || nx < 0 || nx >= outC || visited[ny][nx]) continue
                visited[ny][nx] = true
                if(outerMap[ny][nx]==="") queue.push([ny, nx])
                if(outerMap[ny][nx]===request) outerMap[ny][nx] = ""
            }
        }
    }
    
    for(let i = 0; i < outR; i++){
        for(let j = 0; j < outC; j++){
            if(outerMap[i][j]!=="") answer++;
        }
    }
    return answer;
}