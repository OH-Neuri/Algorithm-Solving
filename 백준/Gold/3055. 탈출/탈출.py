from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

C, R = map(int,input().split())
b_x, b_y = 0, 0
fld = deque()
hedgehog = deque()
h_visited = [[False for _ in range(R)] for _ in range(C)]
arr = []

for i in range(C):
    data = list(input().rstrip())
    # 홍수
    for j in range(len(data)):
        if data[j] == '*':
            fld.append((i,j))
    # 비버 굴
    if 'D' in data:
        b_x, b_y = i, data.index('D')
    # 고슴도치
    if 'S' in data:
        j = data.index('S')
        h_visited[i][j] = True
        hedgehog.append((i, j))
        data[j] = '.'
    arr.append(data)

# 물 이동
def start_flood():
    flood_tmp = deque()
    while fld:
        i, j = fld.popleft()
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]

            if 0<=nx<C and 0<=ny<R and arr[nx][ny] == '.':
                arr[nx][ny] = '*'
                flood_tmp.append((nx,ny))
    fld.extend(flood_tmp)

# 고슴도치 이동
def start_hedgehog():
    hedgehog_tmp = deque()
    while hedgehog:
        i, j = hedgehog.popleft()

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]

            if nx == b_x and ny == b_y:
                return True
            if 0 <= nx < C and 0 <= ny < R and arr[nx][ny] == '.' and not h_visited[nx][ny]:
                h_visited[nx][ny] = True
                hedgehog_tmp.append((nx, ny))

    hedgehog.extend(hedgehog_tmp)
    return False

time = 1
while True:
    start_flood()
    if start_hedgehog():
        print(time)
        break
    else:
        if len(hedgehog) == 0:
            print("KAKTUS")
            break
    time +=1