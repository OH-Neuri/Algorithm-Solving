def solution(d, budget):
    d = sorted(d)
    answer = len(d)
    d_sum = 0
    for i in range(len(d)):
        d_sum += d[i]
        answer = i+1
        if d_sum > budget:
            answer -=1
            break
        else: continue    
    return answer