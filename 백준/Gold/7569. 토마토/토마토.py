from collections import deque
q = deque()
m, n, h = map(int, input().split(' '))
arr = [[] for _ in range(h)]
result = 0

def bfs() :
    move = [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[1,0,0],[-1,0,0]]
    global result

    while q :
        pop = q.popleft()
        xh, xx, xy = pop[0], pop[1], pop[2]

        for i in range(0,6) :
            n_h = move[i][0] + xh #h 높이
            n_x = move[i][1] + xx #n 세로
            n_y = move[i][2] + xy #m 가로

            if n_h <= -1 or n_x <= -1 or n_y <= -1 or n_h >= h or n_x >= n or n_y >= m :
                continue

            if arr[n_h][n_x][n_y] == 0 :
                arr[n_h][n_x][n_y] = arr[xh][xx][xy] + 1
                q.append((n_h,n_x,n_y))
                result += 1

    return result


for i in range(h):
    for _ in range(n):
        arr[i].append(list(map(int, input().split())))

for i in range(h) :
    for j in range(n) :
        for z in range(m) :
            if arr[i][j][z] == 1 :
                q.append((i,j,z))

bfs()

cnt = 0
zeroCnt = 0

for i in range(h) :
    for j in range(n) :
        for z in range(m) :
            if arr[i][j][z] > cnt :
                cnt = arr[i][j][z]
            if arr[i][j][z] == 0 :
                zeroCnt += 1

if zeroCnt > 0 :
    print(-1)
elif result == 0 :
    print(0)
else :
    print(cnt-1)
