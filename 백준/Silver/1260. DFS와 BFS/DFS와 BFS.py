from collections import deque

def DFS(node):
    # 방문처리
    visited[node] = True
    print(node, end = " ")
    # 인접 리스트들 방문 확인
    for x in graph[node]:
        # 방문 안한 정점은 탐색
        if not visited[x]:
            DFS(x)

def BFS(node):
    queue = deque([node])
    # 방문처리
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for x in graph[v]:
            if not visited[x]:
                visited[x]=True
                queue.append(x)


N, M, V = map(int,input().split(" "))
graph = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int,input().split(" "))
    # 양쪽한테 서로 연결되어있다고 알려줘야함 , 지금 한쪽만 아는 상황
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()

# DFS
visited = [False for _ in range(N+1)]
DFS(V)
print()

# BFS
visited = [False for _ in range(N+1)]
BFS(V)
