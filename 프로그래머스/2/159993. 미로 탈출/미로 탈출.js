function solution(maps) {
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]
    const r = maps.length
    const c = maps[0].length
    const start = [0,0]
    const lever = [0,0]
    const end = [0,0] 
    
    for(let i = 0; i < r; i++){
        for(let j = 0; j < c; j++){
            if(maps[i][j] === "S"){
                start[0] = i
                start[1] = j 
            }
            if(maps[i][j] === "L"){
                lever[0] = i
                lever[1] = j 
            }
            if(maps[i][j] === "E"){
                end[0] = i
                end[1] = j 
            }
        }
    }
    const distanceToLever = BFS(start[1], start[0], lever[1], lever[0])
    const distanceToEnd = BFS(lever[1], lever[0], end[1], end[0])
    
    return distanceToLever=== -1 || distanceToEnd === -1 ? -1 : distanceToLever + distanceToEnd;

    
    function BFS(sX, sY, eX, eY){
        const visited = Array.from({length:r}, () => Array(c).fill(false))
        const queue = []
        queue.push([sY, sX, 0])
        visited[sY][sX] = true
        let begin = 0
        while(begin < queue.length){
            // 현재 위치, 이동 횟수
            const [cY, cX, cnt] = queue[begin++]
            
            // 목적지 도착
            if(cY===eY && cX ===eX) return cnt
            
            // 4방향으로 이동
            for(let k = 0; k < 4; k++){
                const ny = cY + dir[k][0]
                const nx = cX + dir[k][1]
                if(ny < 0 || ny >= r || nx < 0 || nx >=c || maps[ny][nx]==="X" || visited[ny][nx]) continue
                visited[ny][nx] = true
                queue.push([ny, nx, cnt + 1])
            }
        }
        
        return -1
    }
}


