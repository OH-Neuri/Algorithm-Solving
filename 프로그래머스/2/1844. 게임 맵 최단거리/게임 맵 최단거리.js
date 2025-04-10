function solution(maps) {
    var answer = -1;
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]
    const row = maps.length
    const col = maps[0].length
    const visited = Array.from({length:row}, ()=> Array.from({length:col}, () => false))
    
    const queue = []
    let begin = 0
    queue.push([0, 0, 1])
    while(begin < queue.length){
        const [cy, cx, cnt] = queue[begin++]
        if(cy === row - 1 && cx === col - 1) return cnt
        
        for(let k = 0; k < 4; k++){
            const ny = cy + dir[k][0]
            const nx = cx + dir[k][1]
            
            if(ny < 0 || ny >= row || nx < 0 || nx >= col || maps[ny][nx] === 0 || visited[ny][nx]) continue
            visited[ny][nx] = true
            queue.push([ny, nx, cnt + 1])
            
        }
    }
    
    return answer;
}