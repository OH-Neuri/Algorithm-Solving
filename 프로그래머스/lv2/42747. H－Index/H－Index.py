def solution(citations):
    answer = 0
    for h in range(1,len(citations)+1):
        cnt = 0
        for x in citations:
        # h번 이상 인용된 논문이 h편 이상이라면
            if h <= x:
                cnt +=1
        if h<=cnt:
            answer = h
            
    return answer