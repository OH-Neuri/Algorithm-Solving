import sys
input = sys.stdin.readline

n = int(input())
p_1, p_2 = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

answer = 0
def DFS(node, depth):
    global answer

    visited[node] = True
    
    if node == p_2:
        answer = depth
        return depth

    for next in graph[node]:
        if not visited[next]:
            DFS(next, depth+1)

DFS(p_1,0)

if visited[p_2]:
    print(answer)
else:
    print(-1)