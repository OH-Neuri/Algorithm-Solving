def solution(board):
    cnt_o = 0
    cnt_x = 0
    win_o = False
    win_x = False
    
    for i in range(3):
        for j in range(3):
            if board[i][j] =="O":
                cnt_o +=1
            elif board[i][j] =='X':
                cnt_x +=1
    
    
    if cnt_o>=cnt_x+2 or cnt_o < cnt_x or (cnt_o > 5 and cnt_x>4):
        return 0
    if (cnt_o==0 and cnt_x==0):
        return 1
    
    
    # 가로
    for i in range(3):
        cnt = 0
        tmp = board[i][0]
        for j in range(1,3):
            if tmp == board[i][j]:
                cnt+=1
        if cnt==2:
            if tmp=='O':
                win_o = True
            if tmp=='X':
                win_x = True
                
    # 세로
    for i in range(3):
        cnt = 0
        tmp = board[0][i]
        for j in range(1,3):
            if tmp == board[j][i]:
                cnt+=1
        if cnt==2:
            if tmp=='O':
                win_o = True
            if tmp=='X':
                win_x = True
    
    # 대각선
    cnt_r = 0
    cnt_l = 0
    
    for i in range(1,3):
        tmp_r = board[0][0]
        if tmp_r == board[i][i]:
            cnt_r+=1
        if cnt_r == 2:
            if tmp_r=='O':
                win_o = True
            if tmp_r=='X':
                win_x = True
        
        tmp_l = board[0][2]
        if tmp_l == board[i][2-i]:
            cnt_l+=1
        if cnt_l == 2:
            if tmp_l=='O':
                win_o = True
            if tmp_l=='X':
                win_x = True
    
    if win_o and win_x:
        if (cnt_x==4 or cnt_o==5):
            return 0
    
    if win_o:
        if win_x:
            return 0
        if cnt_o==cnt_x+1:
            return 1
        else:
            return 0
    if win_x:
        if cnt_o==cnt_x:
            return 1
        else:
            return 0
        
    return 1
