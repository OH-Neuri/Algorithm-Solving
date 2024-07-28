function solution(n, computers) {
    let visited = Array.from({length:n}, ()=>false)
    var answer = 0;
    for(let i=0;i<n;i++){
       if(!visited[i]){
           answer +=1
           DFS(i)
       } 
    }
    function DFS(node){
        visited[node] = true
        
        computers[node].forEach((n, i)=>{
            if(n==1 && !visited[i]) DFS(i)
        })
}
    
    return answer;
}

