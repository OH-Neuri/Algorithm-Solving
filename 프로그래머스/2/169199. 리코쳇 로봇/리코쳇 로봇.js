function solution(board) {
    const dir = [[0,1],[0,-1],[1,0],[-1,0]]
    var answer = 0;
    const row = board.length
    const col = board[0].length
    const start = [0,0]
    const end = [0,0]
    const visited = Array.from({length : row}, () => Array.from({length : col}, ()=> false))
    
    for(let i = 0; i < row; i++){
        for(let j = 0; j < col; j++){
            if(board[i][j]==="R"){
                start[0] = i
                start[1] = j
            }
            if(board[i][j]==="G"){
                end[0] = i
                end[1] = j
            }
        }
    }
        
    const queue = []
    queue.push([start[0], start[1], 0])
    visited[start[0]][start[1]] = true
    let begin = 0
    
    while(begin < queue.length){
        const [cy, cx, cnt] = queue[begin++]
        
        if(cy === end[0] && cx === end[1]) return cnt
        
       
        for(let k = 0; k < 4; k++){
             let ny = cy 
             let nx = cx 
             while(true) {
                const ty = ny + dir[k][0];
                const tx = nx + dir[k][1];
                
                if(ty < 0 || ty >= row || tx < 0 || tx >= col || board[ty][tx] === "D" ) break;
                ny = ty;
                nx = tx;
            }
            
            if(visited[ny][nx]) continue
            visited[ny][nx] = true
            queue.push([ny, nx, cnt + 1])
        }
    }
    
    return -1;
}