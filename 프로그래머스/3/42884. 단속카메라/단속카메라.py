def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:(x[0],x[1]))
    c = -30050
    for s, e in routes:
        if c < s:
            c = e
            answer +=1
        else:
            if e < c:
                c = e
    return answer

# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
