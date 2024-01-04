def solution(people, limit):
    answer = 0
    p = sorted(people,reverse=True)
    l = 0
    r = len(p)-1
    
    while r>l :
        if p[l] + p[r] <= limit:
            l +=1
            r -=1
            answer +=1
            if l>r:
                break
            elif l==r:
                answer +=1
                break
        else:
            l+=1
            answer +=1
            if l==r:
                answer+=1
                break
    return answer
