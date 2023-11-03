
from collections import deque
import copy
# 동,남,서,북
dx = [0,-1,0,1]
dy = [1,0,-1,0]
# 지도의 세로, 지도의 가로
n, m = map(int, input().split())
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))


def bfs():
    q = deque()
    tmp_area = copy.deepcopy(area)
    # 큐에 바이러스 위치 저장
    for i in range(n):
        for j in range(m):
            if tmp_area[i][j] == 2:
                q.append((i,j))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 바이러스 전파 진행
            if 0<=nx<n and 0<=ny<m :
                if tmp_area[nx][ny]==0:
                    tmp_area[nx][ny]=2
                    q.append((nx,ny))
    global result
    count = 0
    # 안전 영역의 최댓값 계산
    for i in range(n):
        for j in range(m):
            if tmp_area[i][j] == 0:
                count+=1
    result = max(result,count)


def make_wall(count):
    # 벽 3개 세우면
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                area[i][j]=1
                make_wall(count+1)
                area[i][j]=0
result = 0
make_wall(0)

print(result)
