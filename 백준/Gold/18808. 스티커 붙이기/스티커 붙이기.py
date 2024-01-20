from copy import deepcopy

# 노트북 크기, 스티커 개수
r, c, k = map(int, input().split())

board = [[0 for _ in range(c)] for _ in range(r)]

sticker_count = []
sticker_list = []
for _ in range(k):
    i, j = map(int, input().split())
    sticker = []
    cnt = 0
    for _ in range(i):
        temp = list(map(int, input().split()))
        sticker.append(temp)
        cnt += temp.count(1)
    sticker_count.append(cnt)
    sticker_list.append(sticker)


def rotate(sticker):
    sticker = deepcopy(sticker)

    n, m = len(sticker), len(sticker[0])
    new_sticker = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if sticker[i][j] == 1:
                new_sticker[j][n - i - 1] = 1

    return new_sticker


def work(sticker, n, m):
    for d in range(4):
        for x in range(0, r):
            for y in range(0, c):
                if stick(x, y, sticker, n, m):
                    return True
        sticker = rotate(sticker)
        n, m = m, n

    return False


def stick(x, y, sticker, n, m):
    for i in range(n):
        for j in range(m):
            if sticker[i][j] == 1:
                if not (0 <= x + i < r and 0 <= y + j < c):
                    return False
                if board[x + i][y + j] == 1:
                    return False
    for i in range(n):
        for j in range(m):
            if sticker[i][j] == 1:
                board[x + i][y + j] = 1

    return True


result = 0
for i in range(len(sticker_list)):
    sticker, sticked = sticker_list[i], sticker_count[i]
    n, m = len(sticker), len(sticker[0])

    if work(sticker, n, m):
        result += sticked

print(result)
