from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 녹는다
def melt():
    q = deque()
    # 빙산이 남은 경우
    for i in range(N):
        for j in range(M):
            melt_cnt = 0
            if arr[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        melt_cnt +=1
                q.append((i,j,melt_cnt))
    if q:
        while q:
            x, y, cnt = q.popleft()
            if arr[x][y]<cnt:
                arr[x][y] = 0
            else:
                arr[x][y] -= cnt
        return True


    # 빙산이 다 녹았을 경우
    else:
        return False

# 덩어리 몇개인지 구분한다
def check():
    flag = False
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                if not visited[i][j]:
                    BFS(i,j,visited)
                    if flag:
                        return True
                    flag = True
                else:
                    continue
    return False

def BFS(i,j,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny]!=0:
                visited[nx][ny] = True
                q.append((nx,ny))

result = 0
while True:
    # 다 녹았으면 종료.
    if not melt():
        result = 0
        break
    result += 1
    # 덩어리가 2개가 되면 종료.
    if check():
        break
print(result)