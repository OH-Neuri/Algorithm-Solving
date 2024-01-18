from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int,input().split())
index = [] # 바이러스 좌표
matrix = [] # 연구소
summ_no_wall= 0
for i in range(n):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        if data[j] == 2:
            index.append([i,j])
    matrix.append(data)
    summ_no_wall += data.count(2)
    summ_no_wall += data.count(0)

def BFS(virus,summ):
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for v in virus:
        q.append(v)
        visited[v[0]][v[1]] = 0
        summ-=1

    max_time = 0
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1 and matrix[nx][ny]!=1:
                visited[nx][ny] = visited[x][y] + 1
                summ-=1
                max_time = max(visited[nx][ny],max_time)
                q.append([nx,ny])

    if summ == 0:
        return max_time
    else:
        return 1e9

result = 1e9
for i in list(combinations(index,m)):
    result = min(result,BFS(i,summ_no_wall))

if result == 1e9:
    print(-1)
else:
    print(result)