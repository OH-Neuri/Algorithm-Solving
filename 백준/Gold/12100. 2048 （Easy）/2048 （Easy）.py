from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split(" "))) for _ in range(N)]

max_value = 0
def game(depth, board, dir):
    # 최대 5번 이동 후
    global max_value
    tmp = []
    if depth == 5:
        for line in board:
            max_value = max( max_value,max(line[:]))
        return

    # 동
    if dir == 0:
        tmp = [arr[:] for arr in board]
        for i in range(N):
            tmp_num = 0
            sum_string = deque() # 이동해서 합산된 숫자들
            for j in range(N-1,-1,-1):
                if board[i][j] != 0:
                    sum_string.appendleft(board[i][j])
                    if tmp_num == board[i][j]:
                        sum_string.popleft();sum_string.popleft()
                        sum_string.appendleft(tmp_num*2)
                        tmp_num = 0
                        continue
                    tmp_num = board[i][j]
            #배열에 넣기

            if sum_string:
                l = len(sum_string)
                for idx in range(N):
                    if idx < N-l:
                        tmp[i][idx] = 0
                    else:
                        tmp[i][idx] = sum_string.popleft()

    # 남
    if dir == 1:
        tmp = [arr[:] for arr in board]
        for i in range(N):
            tmp_num = 0
            sum_string = deque()  # 이동해서 합산된 숫자들
            for j in range(N-1,-1,-1):
                if board[j][i] != 0:
                    sum_string.append(board[j][i])
                    if tmp_num == board[j][i]:
                        sum_string.pop()
                        sum_string.pop()
                        sum_string.append(tmp_num * 2)
                        tmp_num = 0
                        continue
                    tmp_num = board[j][i]

            # 배열에 넣기
            if sum_string:
                l = len(sum_string)
                for idx in range(N-1,-1,-1):
                    if idx > N-1-l:
                        tmp[idx][i] = sum_string.popleft()
                    else:
                        tmp[idx][i] = 0
    # 서
    if dir == 2:
        tmp = [arr[:] for arr in board]
        for i in range(N):
            tmp_num = 0
            sum_string = deque()  # 이동해서 합산된 숫자들
            for j in range(N):
                if board[i][j] != 0:
                    sum_string.append(board[i][j])
                    if tmp_num == board[i][j]:
                        sum_string.pop()
                        sum_string.pop()
                        sum_string.append(tmp_num * 2)
                        tmp_num = 0
                        continue
                    tmp_num = board[i][j]

            #배열에 넣기
            if sum_string:
                l = len(sum_string)
                for idx in range(N):
                    if idx < l:
                        tmp[i][idx] = sum_string.popleft()
                    else:
                        tmp[i][idx] = 0

    # 북
    if dir == 3:
        tmp = [arr[:] for arr in board]
        for i in range(N):
            tmp_num = 0
            sum_string = deque()  # 이동해서 합산된 숫자들
            for j in range(N):
                if board[j][i] != 0:
                    sum_string.appendleft(board[j][i])
                    if tmp_num == board[j][i]:
                        sum_string.popleft()
                        sum_string.popleft()
                        sum_string.appendleft(tmp_num * 2)
                        tmp_num = 0
                        continue
                    tmp_num = board[j][i]
            # 배열에 넣기
            if sum_string:
                l = len(sum_string)
                for idx in range(N):
                    if idx < l:
                        tmp[idx][i] = sum_string.pop()
                    else:
                        tmp[idx][i] = 0

    for i in range(4):
        if depth+1 ==5:
            game(depth+1, tmp, i)
            break
        game(depth + 1, tmp, i)


for i in range(4):
    game(0,board,i)

print(max_value)