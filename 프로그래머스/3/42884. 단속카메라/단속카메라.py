def solution(routes):
    answer = 0
    end = -30001
    
    for s, e in sorted(routes, key=lambda x:x[1]):
        if s>end:
            answer +=1
            end = e
    return answer

# [-20,-15] [-18,-13] [-14,-5] [-5,-3]

