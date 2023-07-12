import sys
input = sys.stdin.readline

N = int(input())
travel_cost = [list(map(int,input().split(" "))) for _ in range(N)]
visited = [0] * N
m = 1e9

def dfs(depth, start, cost):
    global m
    if depth == N-1 and travel_cost[start][0]!=0:
        m = min(m,cost+travel_cost[start][0])
        return
    for i in range(N):
        if not visited[i] and travel_cost[start][i]!=0:
            visited[i]=1
            dfs(depth+1, i, cost + travel_cost[start][i])
            visited[i]=0
visited[0]=1
dfs(0,0,0)
print(m)