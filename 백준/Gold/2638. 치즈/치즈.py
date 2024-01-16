from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
n,m = map(int,input().split())

cheese = []
time = 0
sum_cheese = 0
for _ in range(n):
    data = list(map(int,input().split()))
    sum_cheese += data.count(1)
    cheese.append(data)

while sum_cheese!=0:
    q = deque()
    q.append([0,0])
    melt_tmp = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 1:
                    melt_tmp.append((nx,ny))
                else:
                    q.append((nx,ny))

    melt = deque()
    for x, y in melt_tmp:
        air_cnt = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if visited[nx][ny] and cheese[nx][ny] == 0:
                air_cnt +=1
        if air_cnt >= 2:
            melt.append((x,y))

    for x, y in melt:
        cheese[x][y] = 0
        sum_cheese -=1

    time+=1
print(time)


