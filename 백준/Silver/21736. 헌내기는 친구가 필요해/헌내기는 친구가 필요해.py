import sys
sys.setrecursionlimit(10**6) # 재귀 제한 늘이기
input = sys.stdin.readline

def dfs(x,y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 'P':
        cnt+=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if graph[nx][ny] !="X":
                dfs(nx,ny)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
n,m = map(int,input().split())
graph = list(input() for _ in range(n))
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]=="I":
            dfs(i,j)
if cnt==0:
    print("TT")
else:
    print(cnt)