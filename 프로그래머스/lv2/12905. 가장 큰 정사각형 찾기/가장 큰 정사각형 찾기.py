def solution(board):
    answer = 0
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i+1][j+1] ==1:
                board[i+1][j+1] = min(board[i][j],board[i+1][j],board[i][j+1])+1
                answer = max(answer, board[i+1][j+1])
    if len(board[0])<=2:
        answer = 1
    return answer*answer