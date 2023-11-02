from collections import deque

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]

for i in range(K):
    x, y = map(int,input().split(" "))
    board[x-1][y-1] = 1

D = int(input())
dir = deque([])
for i in range(D):
    t, d = map(str,input().split(" "))
    dir.append((int(t),d))

c_dir = 'r'
x, y = 0, 0
body_list = deque([])
body_list.append((0,0))
tmp_time, tmp_dir = dir.popleft()
t=0
while True:
    if t == tmp_time:
        if tmp_dir =='D':
            if c_dir =='r':
                c_dir='d'
            elif c_dir =='d':
                c_dir='l'
            elif c_dir == 'l':
                c_dir = 'u'
            elif c_dir == 'u':
                c_dir = 'r'
        if tmp_dir =='L':
            if c_dir =='r':
                c_dir='u'
            elif c_dir =='u':
                c_dir='l'
            elif c_dir == 'l':
                c_dir = 'd'
            elif c_dir == 'd':
                c_dir = 'r'
        if dir:
            tmp_time, tmp_dir = dir.popleft()

    if c_dir =='r':
        y+=1
    if c_dir =='d':
        x+=1
    if c_dir =='l':
        y-=1
    if c_dir =='u':
        x-=1

    # 배열에 안나가고 꼬리를 안밟으면 오케이
    if 0<=x<N and 0<=y<N and (x,y) not in body_list:
        t+=1
        body_list.appendleft((x,y))
        if board[x][y]!=1:
            c, l = body_list.pop()
            board[c][l] = 0
    else:
        break

print(t+1)