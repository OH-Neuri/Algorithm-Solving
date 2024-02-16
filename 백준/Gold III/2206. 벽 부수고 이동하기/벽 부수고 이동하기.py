from collections import deque
import sys

input = sys.stdin.readline

def BFS():
    q = deque()
    q.append((0, 0, 0, 1, 1))  # x, y, 상태, 거리, 경로번호
    visited[(0,0)] = [1]
    global min_dist
    while q:
        x, y, s, dist, num = q.popleft()
        if x == N - 1 and y == M - 1:           # 도착
            min_dist = min(dist,min_dist)      # 최단거리 갱신


        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and num not in visited[(nx,ny)]:
                if matrix[nx][ny] == 1:  # 벽 만남
                    if s == 0:
                        visited[(nx,ny)].append(num+1)
                        q.append((nx, ny, 1, dist + 1, num+1))
                else:
                    visited[(nx, ny)].append(num)
                    q.append((nx, ny, s, dist + 1,num))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
visited = {}
for i in range(N):
    for j in range(M):
        visited[(i,j)] = []
min_dist = 1e9

BFS()
if min_dist == 1e9:
    print(-1)
else:
    print(min_dist)
