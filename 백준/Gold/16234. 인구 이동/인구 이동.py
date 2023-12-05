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
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                value_list.append(BFS(i,j,visited))

    # 더이상 연합이 생성되지 않는 경우
    if len(value_list)==N*M:
        return False
    else:
        return value_list

def BFS(i,j,visited):
    q = deque()
    q.append((i,j))
    value = arr[i][j]
    visited[i][j] = True
    position = [(i,j)]
    cnt = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if L<=abs(arr[x][y]-arr[nx][ny])<=R:
                    cnt+=1
                    visited[nx][ny] = True
                    position.append((nx,ny))
                    value += arr[nx][ny]
                    q.append((nx,ny))

    return (value,cnt,position)

answer = 0
while True:
    # 더이상 연합을 만들 수 없을 때
    result = make_alliance()
    if not result:
        break
    else:
    # 인구이동
        for value, cnt, positions in result:
            if cnt == 1:
                continue
            for x, y in positions:
                arr[x][y] = value // cnt
    answer +=1

print(answer)
