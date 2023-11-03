
from collections import deque
# 시험관 크기, 바이러스 개수
N, K = map(int,input().split())
graph = [] # 시험관 정보 리스트
data = [] # 바이러스 정보 리스트

for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 위치X, 위치Y
            data.append((graph[i][j],0,i,j))

data = sorted(data)
q = deque(data)

S, X, Y = map(int,input().split())

# 동, 남, 서, 북
dx = [0,-1,0,1]
dy = [1,0,-1,0]

while q:
    virus, time, x, y = q.popleft()
    # 정확히 S초가 지나거나, 큐가 빌 때 까지 반복
    if time == S:
        break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny]==0:
            graph[nx][ny] = virus
            q.append((virus,time+1,nx,ny))

print(graph[X-1][Y-1])
