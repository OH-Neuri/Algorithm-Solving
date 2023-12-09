import sys
input = sys.stdin.readline

# 동, 서, 북, 남
dx = [0,0,-1,+1]
dy = [1,-1,0,0]
idx = [(1,0),(1,1),(1,2),(3,1)]
N, M, X, Y, K = map(int,input().split()) # 세로, 가로, 주사위 좌표

arr = [] # 지도
for _ in range(N):
    arr.append(list(map(int,input().split())))

dir = list(map(int,input().split())) # 이동순서 (-1)
dice = [[0 for _ in range(3)] for _ in range(4)] # 주사위
for d in dir:

    # 이동 좌표
    nx = X+dx[d-1]
    ny = Y+dy[d-1]

    # 이동 좌표가 배열 범위 안에 있는 경우
    if  0<=nx<N and 0<=ny<M:

        X, Y = nx, ny # 이동

        # 굴린다
        # 좌, 우
        if d < 3:
            # 좌
            if d == 1:
                tmp = dice[1][0]
                for i in range(3):
                    dice[idx[i][0]][idx[i][1]] = dice[idx[i+1][0]][idx[i+1][1]]
                dice[3][1] = tmp
            # 우
            if d == 2:
                tmp = dice[3][1]
                for i in range(3,-1,-1):
                    dice[idx[i][0]][idx[i][1]] = dice[idx[i-1][0]][idx[i-1][1]]
                dice[1][0] = tmp
        # 상, 하
        else:
            # 상
            if d == 3:
                tmp = dice[0][1]
                for i in range(3):
                    dice[i][1] = dice[i+1][1]
                dice[3][1] = tmp
            # 하
            if d == 4:
                tmp = dice[3][1]
                for i in range(3,-1,-1):
                    dice[i][1] = dice[i-1][1]
                dice[0][1] = tmp

        # 윗 면 출력
        print(dice[1][1])

        # 복사한다
        # 좌표가 0이면 주사위 숫자 복사
        if arr[X][Y] == 0:
            arr[X][Y] = dice[3][1]
    
        # 좌표가 0이 아니면 주사위에 복사되고 해당 자리 0
        else:
            dice[3][1] = arr[X][Y]
            arr[X][Y] = 0

