import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx,ny])

M,N = map(int,input().split(" "))
box = []
for _ in range(N):
    box.append(list(map(int,input().split(" "))))

q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i,j])

bfs()
max_day = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    max_day = max(max_day,max(i))
print(max_day - 1)