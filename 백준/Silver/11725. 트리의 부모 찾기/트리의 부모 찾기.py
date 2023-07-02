import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

def DFS(node):
    for x in tree[node]:
        if not parent[x]:
            parent[x] = node
            DFS(x)

for i in range(N-1):
    node_a, node_b  = map(int, sys.stdin.readline().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

DFS(1)
for i in range(2,N+1):
    print(parent[i])
