from collections import deque
import sys

input = sys.stdin.readline

def BFS():
    q = deque()
    q.append((0, 0, 0, 1))  # x, y, 상태, 거리
    visited[0][0][0] = True
    global min_dist
    while q:
        x, y, s, dist = q.popleft()
        if x == N - 1 and y == M - 1:          # 도착
            min_dist = min(dist,min_dist)      # 최단거리 갱신


        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if s==1 and matrix[nx][ny]!=1 and not visited[nx][ny][1]:         # 이미 벽을 뚫고온 경우!
                    visited[nx][ny][s] = True
                    q.append((nx,ny,s,dist+1))
                elif s==0 and not visited[nx][ny][0]:                             # 아직 한번도 안뚫은 경우!
                    if matrix[nx][ny] ==1:
                        visited[nx][ny][1] = True
                        q.append((nx,ny,1,dist+1))
                    else:
                        visited[nx][ny][0] = True
                        q.append((nx,ny,0,dist+1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

min_dist = 1e9

BFS()
if min_dist == 1e9:
    print(-1)
else:
    print(min_dist)
