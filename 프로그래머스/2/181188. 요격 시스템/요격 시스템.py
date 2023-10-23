def solution(targets):
    answer, end = 0, 0
    
    for s, e in sorted(targets, key=lambda x:x[1]):
        if s >= end:
            answer+=1
            end = e
    return answer