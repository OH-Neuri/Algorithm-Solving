function solution(land) {
    
    const rLen = land.length
    const cLen = land[0].length
    
    const dc = [1,0,-1,0]
    const dr = [0,1,0,-1]
    
    const retAry = Array(cLen).fill(0)
    
    const dfs = (r,c) => {
        let ret = 0
        const stk = [[r,c]]
        let minC = c
        let maxC = c
        
        while(stk.length){
            const [r,c] = stk.pop()
            minC = Math.min(c,minC)
            maxC = Math.max(c,maxC)
            if(visited[r][c]) continue
            visited[r][c] = true
            ret += 1
            for (let d = 0 ; d < 4 ; d++){
                const [nR,nC] = [r + dr[d] , c + dc[d]]
                if(0<=nR&&nR<rLen&&0<=nC&&nC<cLen&&!visited[nR][nC]&&land[nR][nC]===1){
                    stk.push([nR,nC])
                }
            }
        }
        
        for (let i = minC ; i <= maxC ; i++){
            retAry[i] += ret
        }
    }
    
    
    
    const visited= new Array(rLen).fill().map(_ => new Array(cLen).fill(0));
    for (let i = 0 ; i < rLen ; i++){
        for (let j = 0 ; j < cLen ; j++){
            if(!visited[i][j]&&land[i][j]===1){
                dfs(i,j)
            }
        }
    }
    
    return Math.max(...retAry)
    
}