from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

T = int(input()) # 테케
for _ in range(T):
    # 가로, 세로, 위치개수
    M, N, K = map(int,input().split())
    arr = [[False for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        i, j = map(int,input().split())
        arr[j][i] = True

    answer = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j]:
                answer +=1
                BFS(i,j)

    print(answer)