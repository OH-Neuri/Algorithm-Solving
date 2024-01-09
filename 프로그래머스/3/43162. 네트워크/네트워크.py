def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,i):
            if i==j:
                continue
            if computers[i-1][j-1]==1:
                graph[i].append(j)
                graph[j].append(i)
    
    def DFS(node):
        visited[node] = True
        for next in graph[node]:
            if not visited[next]:
                DFS(next)
                
    visited = [False for _ in range(n+1)]
    
    for i in range(1, n+1):
        if not visited[i]:
            DFS(i)
            answer +=1
    
    return answer
