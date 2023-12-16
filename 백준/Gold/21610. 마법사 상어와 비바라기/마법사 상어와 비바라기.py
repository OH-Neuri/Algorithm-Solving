import copy
import sys
input = sys.stdin.readline


dir = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

N, M = map(int,input().split())

# 칸
arr = [list(map(int,input().split())) for _ in range(N)]
# 방향, 거리
data = [list(map(int,input().split())) for _ in range(M)] #[[1,3] [3,4],[8,1],[4,8]]
# 구름 위치
cloud = [[False for _ in range(N)] for _ in range(N)]

# 구름 초기 위치
for i in range(N-2,N):
    for j in range(2):
        cloud[i][j] = True

for tc in range(M):
    # 구름 이동
    tmp = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                x, y = i, j

                nx = x + data[tc][1]*dir[data[tc][0]][0]
                ny = y + data[tc][1]*dir[data[tc][0]][1]

                if nx >= N or nx <0:
                    nx %= N
                if ny >= N or ny <0:
                    ny %= N

                x, y = nx, ny
                # 구름 이동 위치 저장
                tmp[x][y] = True
                # 구름 사라지면서 비 1씩 내리기
                arr[x][y] += 1
                # 대각선 확인하기

    cloud = copy.deepcopy(tmp)
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                for k in range(2,10,2):
                    nx = i + dir[k][0]
                    ny = j + dir[k][1]
                    # 대각선 위치에 물이 있다면 1 증가
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] != 0:
                        arr[i][j]+=1
    # 물의 양 2이상인 칸에 구름 저장
    tmp = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not cloud[i][j]:
                arr[i][j] -= 2
                tmp[i][j] = True

    cloud = copy.deepcopy(tmp)

answer = 0
for i in range(N):
    for j in range(N):
        answer += arr[i][j]

print(answer)
