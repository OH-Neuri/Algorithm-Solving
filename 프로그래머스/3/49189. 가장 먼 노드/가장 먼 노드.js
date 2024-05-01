function solution(n, edge) {
    let visited = Array.from({length:n+1},()=>0)
    let graph = Array.from({length:n+1},()=>[])
    visited[1] = 1
    
    for(let [s,e] of edge){
        graph[s].push(e)
        graph[e].push(s)
    }
    
    let max = 0
    const BFS = () =>{
        let queue = [[1,1]]
        while(queue.length){
            let [cn,ct] = queue.shift()
            
            for(let next of graph[cn]){
                if(!visited[next]){
                    visited[next] = ct+1
                    queue.push([next,ct+1])
                }
            }
        }
    }
    
    BFS()
    var answer = 0;
    
    let maxVisited = Math.max(...visited)
    for(let v of visited){
        if(v===maxVisited) answer +=1
    }

    return answer;
}