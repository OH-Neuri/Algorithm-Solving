// 각 섬 BFS 돌려서 며칠씩 머무를 수 있는지 찾기
function solution(maps) {
    var answer = [];
    const row = maps.length
    const col = maps[0].length
    const visited = Array.from({length:row}, ()=> Array.from({length:col}, ()=> false))
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]

    for(let i = 0; i < row; i++){
        for(let j = 0; j < col; j++){
            if(!visited[i][j] && maps[i][j]!=="X") {
                const maxDays = BFS(i,j)
                console.log(maxDays)
                answer.push(maxDays)
            }
        }
    }
    
    function BFS(y, x){
        const queue = []
        visited[y][x] = true
        queue.push([y, x])
        let days = Number(maps[y][x])
        let begin = 0
        while(begin < queue.length){
            const [cy, cx] = queue[begin++]
            for(let k = 0; k < 4; k++){
                const ny = cy + dir[k][0]
                const nx = cx + dir[k][1]
                
                if(ny < 0 || ny >= row || nx < 0 || nx >= col 
                   || maps[ny][nx]==="X" || visited[ny][nx]) continue
                
                visited[ny][nx] = true
                days += Number(maps[ny][nx])
                queue.push([ny, nx])
            }
        }
        return days
    }
    
    if(!answer.length) return [-1]
    else return answer.sort((a, b) => a - b)
}