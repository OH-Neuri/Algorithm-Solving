function solution(land) {
    var answer = 0;
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]
    const row = land.length
    const col = land[0].length
    const visited = Array.from({length:row}, () => Array.from({length:col}, () => 0))
    const oil = new Map() // 석유 
    let oilNum = 1
    
    for(let i = 0; i < row; i++){
        for(let j = 0 ; j < col; j++){
            if(land[i][j] && !visited[i][j]){
                const oilMass = BFS(i, j, oilNum)
                oil.set(oilNum, oilMass)
                oilNum++;
            }
        }
    }
    
    for(let i = 0; i < col; i++){
        let oilSum = 0 // 시추관이 뽑을 수 있는 석유량
        const visitedOilNum = new Set() // 뽑은 석유 덩어리 번호들
        
        for(let j = 0; j < row; j++){
            // 석유 없는 경우 패스
            if(!land[j][i]) continue 
            
            const oilNum = visited[j][i] // 석유 덩어리 번호 
            // 이미 뽑은 석유일 경우 패스 
            if(visitedOilNum.has(oilNum)) continue
            
            oilSum += oil.get(oilNum)
            visitedOilNum.add(oilNum)
        }
        answer = Math.max(answer, oilSum)
    }
    
    function BFS(i, j, oilNum){
        let mass = 1
        const queue = []
        queue.push([i, j])
        visited[i][j] = oilNum
        let begin = 0
        while(begin < queue.length){
            const [cy, cx] = queue[begin++]
            
            for(let k = 0; k < 4; k++){
                const ny = cy + dir[k][0]
                const nx = cx + dir[k][1]
                
                if(ny < 0 || ny >= row || nx < 0 || nx >= col || visited[ny][nx]!==0
                  || !land[ny][nx]) continue
                
                visited[ny][nx] = oilNum
                queue.push([ny, nx])
                mass++;
            }
        }
        return mass
    }
    
    return answer;
}