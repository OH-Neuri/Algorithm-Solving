def solution(storey):
    answer = 0
    while storey >0:
        # 1의 자리수로 올리고 내리는거 판단한 후,
        # 0이 될 때까지 카운트하기
        storey, move = divmod(storey, 10)
        if move > 5 or (move==5 and storey % 10 >=5): 
            move = 10-move
            storey +=1
        answer += move
    
    return answer
    