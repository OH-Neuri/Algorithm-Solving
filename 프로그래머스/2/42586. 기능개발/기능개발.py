def solution(progresses, speeds):
    day = 1
    distribute = 0
    answer = []
    for p, s in zip(progresses,speeds):
        if p + (s * day) < 100:
            if distribute:
                answer.append(distribute)
                distribute = 0
            while p + (s * day) <100:
                day+=1
            distribute = 1
        else:
            distribute +=1
    answer.append(distribute)
    
    return answer