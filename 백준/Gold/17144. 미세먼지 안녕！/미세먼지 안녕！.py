import sys
input = sys.stdin.readline

# R: 가로, C: 세로, T: 시간
R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]

# 공기 청정기 위치
cleaner_up = -1
cleaner_down = -1
for i in range(R):
    if room[i][0] == -1:
        cleaner_up = i
        cleaner_down = i+1
        break

# 확산
def spread():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    tmp_arr = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<R and 0<=ny<C and room[nx][ny]!=-1:
                        tmp_arr[nx][ny] += room[i][j]//5
                        tmp += room[i][j]//5
                room[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            room[i][j] += tmp_arr[i][j]

# 위로 순환
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner_up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner_up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner_down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner_down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny

for _ in range(T):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            answer += room[i][j]

print(answer)