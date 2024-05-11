function solution(n, roads, sources, destination) {
    let graph = Array.from({length : n + 1}, () =>[])
    let visited = Array.from({length : n + 1}, () => -1)
    
    for(let [s, e] of roads) {
        graph[e].push(s)
        graph[s].push(e)
    }
    let queue = [[destination,0]]
    
    while(queue.length){
        let [curr, cnt] = queue.shift()
        
        // 출발지와 도착지가 같은 경우
        if(visited[curr]===-1 && curr===destination){
            visited[curr] = 0
        }
        
        for (let next of graph[curr]){
            if(visited[next]===-1){
                visited[next] = cnt+1
                queue.push([next,cnt+1])
            } 
        }
    }
    var answer = [];
    for(let source of sources){
        answer.push(visited[source])
    }
    return answer;
    
}
