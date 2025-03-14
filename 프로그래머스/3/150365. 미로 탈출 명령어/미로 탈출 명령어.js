function solution(n, m, x, y, r, c, k) {
    const dir = [[1,0],[0,-1],[0,1],[-1,0]] // d, l, r, u
    const dirStr = ["d","l","r","u"]
    
    if ((x + y + r + c) % 2 !== k % 2 || Math.abs(r - x) + Math.abs(c - y) > k) {
    return "impossible";
    }
    
    // 방문 여부 체크
    const visited = Array.from({ length: n }, () =>
        Array.from({ length: m }, () => new Set())
    );
    
    const queue = []
    queue.push([x-1,y-1,""]) // 좌표, 경로
    visited[y-1][x-1].add(0)
    let begin = 0
    while(begin<queue.length){
        const [cy, cx, path] = queue[begin++]
        
        // 목표 지점 도착
        if(cy===r-1 && cx===c-1 && path.length ===k) return path
        
        for(let i=0;i<4;i++){
            const ny = cy + dir[i][0]
            const nx = cx + dir[i][1]
            const newPath = path + dirStr[i]
            
            if(ny<0 || ny>=n || nx<0 || nx >=m) continue
            
            const remainingSteps = k - newPath.length
            const newMinDist = Math.abs(ny - (r - 1)) + Math.abs(nx - (c - 1));
            if((remainingSteps-newMinDist) % 2 !== 0) continue
            if(visited[ny][nx].has(newPath.length)) continue;
            visited[ny][nx].add(newPath.length)
            
            queue.push([ny,nx,newPath])
            
        }
    }
    
    return "impossible";
}

// 갔던 곳 또 갈 수 있다 그래서 방문체크 안함, 근데 왜 해야하지?
// 사전순으로 탐색하게했는데 왜 이게 최적해를 보장하지 않음?

