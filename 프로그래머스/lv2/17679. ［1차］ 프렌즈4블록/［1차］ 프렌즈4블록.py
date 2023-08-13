def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    
    cnt = 0
    rm = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                # 빈칸은 카운트 안함
                if t == []:
                    continue
                if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i,j))
                    rm.add((i+1,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j+1))
        
        # 2*2 블럭이 존재한다면 좌표 개수 세주고 블럭 지우기
        if rm:
            cnt += len(rm)
            print(cnt)
            for i,j in rm:
                board[i][j] = []
            rm = set()
        else: 
            return cnt
                
        # 위에서 내려오면서 블럭 내리기
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved ==0:
                break
