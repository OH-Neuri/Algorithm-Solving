def solution(n, computers):
    # n : 노드 수
    # computers : 연결 정보 2차원 배열
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[i])): 
            if computers[i][j]==1: 
                graph[i+1].append(j+1)
                
    def DFS(node):
        # 방문처리
        visited[node] = True
        for x in graph[node]:
            # 아직 방문 안했으면 고
            if visited[x]==False:
                DFS(x)
    
    visited = [False for _ in range(n+1)]
    
    for i in range(1, n+1):
        if visited[i]==False:
            DFS(i)
            answer +=1
    
    return answer