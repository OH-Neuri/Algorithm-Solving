import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(node):
    visited[node] = True
    for x in graph[node]:
        if not visited[x]:
            DFS(x)

N, M = map(int,input().split(" "))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split(" "))
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(N+1)]
answer = 0

for i in range(1, N+1):
    if visited[i]==False:
        answer +=1
        DFS(i)
        
print(answer)