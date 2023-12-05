from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
M = len(arr[0])

# 국경선 열기(연합찾기)
def make_alliance():
    value_list = []
    visited = [[False]*M for _ in range(N)]

    flag = False

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if(BFS(i,j,visited)):
                    flag = True

    # 더이상 연합이 생성되지 않는 경우
    return flag

def BFS(i,j,visited):
    q = deque()
    q.append((i,j))
    value = arr[i][j]
    visited[i][j] = True
    position = [(i,j)]
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if L<=abs(arr[x][y]-arr[nx][ny])<=R:
                    visited[nx][ny] = True
                    position.append((nx,ny))
                    value += arr[nx][ny]
                    q.append((nx,ny))

    length = len(position)
    for x,y in position:
        arr[x][y] = value//length

    return length >= 2
answer = 0
while True:
    # 더이상 연합을 만들 수 없을 때
    result = make_alliance()
    if not result:
        break
    answer +=1

print(answer)
