import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())

def DFS(node):
    for a, b in graph[node]:
        if visited[a] == -1:
            visited[a] = visited[node] + b
            if _max[1] < visited[a]:
                _max[1] = visited[a]
                _max[0] = a
            DFS(a)

graph = [[] for _ in range(N+1)]


for _ in range(N):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

visited = [-1 for _ in range(N+1)]
_max = [0,0]
visited[1] = 0
DFS(1)

start = _max[0]
visited = [-1 for _ in range(N+1)]
_max = [0,0]
visited[start] = 0
DFS(start)
print(_max[1])





