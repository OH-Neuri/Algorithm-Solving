function solution(n, computers) {
    let visited = Array.from({length:n},()=>false)

    //탐색 시작
    const DFS = (node) => {
        visited[node] = true
        for(let i=0;i<n;i++){
            if(!visited[i] && computers[node][i]===1){
                DFS(i)
            }
        }
    } 
    //방문 처리
    let answer = 0
    for(let i=0;i<n;i++){
        if(!visited[i]){
            DFS(i);
            answer +=1
        }
    }
    return answer;
}
