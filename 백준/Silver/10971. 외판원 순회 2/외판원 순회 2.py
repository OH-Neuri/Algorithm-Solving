import sys
input = sys.stdin.readline

N = int(input())
travel_cost = [list(map(int,input().split(" "))) for _ in range(N)]
visited_index = []
visited = [0] * N
m = 1e9

def dfs(depth, start, init):
    global m
    if depth == N and travel_cost[start][init]!=0:
        m = min(m,sum(visited_index)+travel_cost[start][init])
        return
    for i in range(N):
        if not visited[i] and travel_cost[start][i]!=0:
            visited[i]=1
            visited_index.append(travel_cost[start][i])
            dfs(depth+1, i, init)
            # 다음 i 가기 전 초기화
            visited_index.pop()
            visited[i]=0
for i in range(N):
    visited[i]=1
    dfs(1,i,i)
    # 다음 i 가기 전 초기화
    visited[i]=0
print(m)