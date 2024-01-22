import sys
input = sys.stdin.readline

info = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, -1, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]

N = int(input())  # 칸 수
matrix = [list(map(int,input().split())) for _ in range(N)] # 모래밭
total_sand = 0 # 격자 밖으로 나간 모래 양
x, y = N // 2, N // 2

# x, y : 좌표
# info : 비율 배열
def scatter(x, y, info):
    if matrix[x][y] == 0:
        return 0

    sand = 0
    a = matrix[x][y]
    xy_sand = matrix[x][y]
    a_x, a_y = -1, -1
    matrix[x][y] = 0
    for c in range(5):
        for r in range(5):
            nx, ny = x + c - 2, y + r - 2
            if info[c][r] == -1:
                if 0<=nx<N and 0<=ny<N:
                    a_x, a_y = nx, ny
                continue
            move_sand = int(xy_sand * info[c][r])
            a -= move_sand
            # 모래밭 안에 있는 경우
            if 0<=nx<N and 0<=ny<N:
                matrix[nx][ny] += move_sand
            # 모래밭을 나간 경우
            else:
                sand += move_sand
    if a_x == -1 and a_y == -1:
        sand += a
    else:
        matrix[a_x][a_y] += a

    return sand

for k in range(2, N, 2):
    # 왼쪽
    for i in range(1, k):
        x, y = x, y - 1
        if matrix[x][y]:
            total_sand += scatter(x,y,info)

    # 아래쪽
    info = list(map(list, zip(*info)))[::-1]
    for i in range(1, k):
        x, y = x + 1, y
        if matrix[x][y]:
            total_sand += scatter(x,y,info)

    # 오른쪽
    info = list(map(list, zip(*info)))[::-1]
    for i in range(1, k + 1):
        x, y = x, y + 1
        if matrix[x][y]:
            total_sand += scatter(x,y,info)

    #윗쪽
    info = list(map(list, zip(*info)))[::-1]
    for i in range(1, k + 1):
        x, y = x - 1, y
        if matrix[x][y]:
            total_sand += scatter(x,y,info)

    info = list(map(list, zip(*info)))[::-1]

for i in range(1, N):
    x, y = x, y - 1
    total_sand += scatter(x,y,info)

print(total_sand)