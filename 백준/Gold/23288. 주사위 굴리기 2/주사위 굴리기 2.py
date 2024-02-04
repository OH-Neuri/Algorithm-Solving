from collections import deque
import sys

input = sys.stdin.readline

# 증가 : 시계방향, 감소 : 반시계방향
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
dice_dir = 0  # 동
d_x, d_y = 0, 0
score = 0


def move_dice(dir):
    if dir == 0:  # 동
        tmp = dice[1][2]
        dice[1][2], dice[1][1],dice[1][0] = dice[1][1], dice[1][0],dice[3][1]
        dice[3][1] = tmp
    if dir == 1:  # 남
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = tmp
    if dir == 2:  # 서
        tmp = dice[1][0]
        dice[1][0], dice[1][1],dice[1][2] = dice[1][1], dice[1][2],dice[3][1]
        dice[3][1] = tmp
    if dir == 3:  # 북
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = tmp



def get_score(i,j,s):
    q = deque()
    q.append((i,j))
    visited = [[False]*M for _ in range(N)]
    visited[i][j] = True
    score = s
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == s and not visited[nx][ny]:
                visited[nx][ny] = True
                score+=s
                q.append((nx,ny))
    return score

for k in range(K):
    # 주사위 이동
    nx, ny =  d_x + dx[dice_dir], d_y + dy[dice_dir]
    if nx <0 or nx >= N or ny<0 or ny>=M:     # 배열을 벗어나면 반대 방향으로 전환
        if dice_dir % 2 ==0:
            dice_dir = 0 if dice_dir==2 else 2
        else:
            dice_dir = 1 if dice_dir == 3 else 3
        d_x, d_y = d_x + dx[dice_dir] , d_y + dy[dice_dir] # 주사위 이동
    else:
        d_x, d_y = nx, ny # 주사위 이동
    # 주사위 번호 갱신
    move_dice(dice_dir)

    # 주사위가 도착한 칸
    board_num = board[d_x][d_y]

    # 점수 획득
    score += get_score(d_x,d_y,board_num)

    # 이동방향 결정
    dice_num = dice[3][1]
    if dice_num > board_num: # 주사위 번호가 더 큰 경우
        dice_dir = (dice_dir+1)%4
    elif dice_num < board_num: # 주사위 번호가 작은 경우
        dice_dir = (dice_dir-1)%4
print(score)