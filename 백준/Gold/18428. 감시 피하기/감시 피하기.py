# 장애물놓기
# 선생님 좌표에서 상하좌우 확인하기
import sys
input = sys.stdin.readline

# 동,남,서,북
dx = [0,-1,0,1]
dy = [1,0,-1,0]

N = int(input())
school = []
T = []
for i in range(N):
    school.append(list(map(str, input().split())))
    for j in range(N):
        if school[i][j] =='T':
            T.append((i,j))


def make_wall(count):
    if count==3:
        # 선생님 좌표에서 탐색 시작
        for x, y in T:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                while 0<=nx<N and 0<=ny<N:
                    # 학생을 만나면 종료
                    if school[nx][ny] == 'S':
                        return False
                    # 장애물, 선생님 만나면 계속
                    if school[nx][ny]!='X':
                        break
                    nx += dx[k]
                    ny += dy[k]
        return True

    for i in range(N):
        for j in range(N):
            if school[i][j]=='X':
                tmp = school[i][j]
                school[i][j]='O'
                count+=1
                if make_wall(count):
                    return True
                school[i][j] = tmp
                count-=1

if make_wall(0):
    print('YES')
else:
    print('NO')