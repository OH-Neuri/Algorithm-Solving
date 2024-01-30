import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

# N : 0, E : 1, S: 2, W : 3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
robots = {}
for i in range(1, N + 1):
    x, y, d = map(str, input().rstrip().split())
    if d == 'N':
        d = 0
    if d == 'E':
        d = 1
    if d == 'S':
        d = 2
    if d == 'W':
        d = 3
    robots[i] = [(int(x), int(y)), d]

for _ in range(M):
    rb_num, rb_d, times = map(str, input().rstrip().split())
    rb_num = int(rb_num)
    times = int(times)

    fail1 = False # 배열 밖으로 나가는 경우 실패
    x, y, d = robots[rb_num][0][0], robots[rb_num][0][1], robots[rb_num][1]
    for _ in range(times):
        fail2 = -1 # 로봇끼리 충돌한 경우 실패
        if rb_d == 'L':
            d = (d - 1) % 4
        if rb_d == 'R':
            d = (d + 1) % 4
        if rb_d == 'F':
            nx, ny = x + dx[d], y + dy[d]
            if 0 < nx <= A and 0 < ny <= B:
                for i in range(1,len(robots)+1):
                    if i != rb_num and (nx,ny) == robots[i][0]: # 로봇끼리 충돌한 경우
                        fail2 = i
                        break
            else: # 배열 밖으로 나간 경우
                fail1 = True
                break
            x, y = nx, ny
        if fail2 != -1:
            print(f"Robot {rb_num} crashes into robot {fail2}")
            exit(0)
    if fail1 :
        print(f"Robot {rb_num} crashes into the wall")
        exit(0)
    else:
        robots[rb_num][0] = (x, y)
        robots[rb_num][1] = d

print("OK")