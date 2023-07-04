import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(node):
    for a, b in tree[node]:
        if visited[a] == -1:
            visited[a] = visited[node] + b
            DFS(a)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        tree[c[0]].append((c[e], c[e + 1]))

visited = [-1 for _ in range(N+1)]
visited[1] = 0
DFS(1)
max_node = visited.index(max(visited))

visited = [-1 for _ in range(N+1)]
visited[max_node] = 0
DFS(max_node)
print(max(visited))