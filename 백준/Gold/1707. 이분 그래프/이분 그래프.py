import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def check_bipartite(node, color):
    global answer

    if answer == "NO":
        return

    visited[node] = color
    for x in graph[node]:
        if not visited[x]:
            check_bipartite(x, -color)
        elif visited[node]==visited[x]:
            answer = "NO"
            return

K = int(input())
for _ in range(K):

    V, E = map(int,input().split(" "))
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    answer = "YES"

    for _ in range(E):
        s, e = map(int,input().split(" "))
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1,V+1):
        if not visited[i]:
            check_bipartite(i, 1)
            if answer == "NO":
                break
    print(answer)


