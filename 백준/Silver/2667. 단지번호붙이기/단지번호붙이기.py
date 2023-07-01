import sys
from collections import deque
sys.setrecursionlimit(10**7)

dx =[0,1,0,-1]
dy =[-1,0,1,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    house = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    house +=1
                    q.append((nx,ny))
    return house

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i,j))

cnt.sort()
print(len(cnt))
for x in cnt:
    print(x)