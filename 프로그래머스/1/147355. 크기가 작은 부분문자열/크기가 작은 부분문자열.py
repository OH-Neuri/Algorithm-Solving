def solution(t, p):
    t_l = len(t)
    p_l = len(p)
    answer = 0
    
    for i in range(t_l-p_l+1):
        if int(t[i:i+p_l]) <= int(p):
            answer +=1
    return answer