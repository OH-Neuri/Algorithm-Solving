import sys
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def DFS(node):
    visited[node]=True
    for x in graph[node]:
        if not visited[x]:
            DFS(x)

T = int(input())
for _ in range(T):

    N = int(input())
    end = list(map(int,input().split(" ")))
    graph = [[] for _ in range(N+1)]

    for i in range(N):
        graph[i+1].append(end[i])

    visited = [False for _ in range(N+1)]
    permutation_cycle = 0

    for i in range(1,N+1):
        if not visited[i]:
            permutation_cycle +=1
            DFS(i)
    print(permutation_cycle)