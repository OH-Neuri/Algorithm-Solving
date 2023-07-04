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
for _ in range(N-1):
    a, b, c = map(int,input().split(" "))
    tree[a].append((b,c))
    tree[b].append((a,c))

visited = [-1 for _ in range(N+1)]
visited[1] = 0
DFS(1)
max_node = visited.index(max(visited))

visited = [-1 for _ in range(N+1)]
visited[max_node] = 0
DFS(max_node)
print(max(visited))