from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def BFS(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    area = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                area +=1
                q.append((nx,ny))
    return area

p_cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            p_cnt +=1
            max_area = max(BFS(i,j),max_area)

print(p_cnt)
print(max_area)
