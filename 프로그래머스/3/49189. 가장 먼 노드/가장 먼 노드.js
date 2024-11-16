function solution(n, edge) {
    
    let graph = Array.from({length:n+1},()=>[])
    for(let [s,e] of edge){
        graph[s].push(e)
        graph[e].push(s)
    }
    
    let maxDist = 0
    let visited = Array(n+1).fill(0)
    visited[1] = 1
    
    let queue = []
    let begin = 0
    let end = 1
    queue.push([1]) // node
    
    while(begin < end){
        const curr = queue[begin++]
        
        maxDist = Math.max(maxDist, visited[curr])
        
        for(let next of graph[curr]){
            if(visited[next]==0){
                visited[next] = visited[curr] + 1;
                queue.push([next])
                end++;
            }
        }
    }
    
    let maxCnt = 0
    visited.sort((a,b)=>b-a)
    for(let num of visited){
        if(visited[0]===num) {
            maxCnt++
        }
        else{ 
            break
        }
    }

    return maxCnt;
}
