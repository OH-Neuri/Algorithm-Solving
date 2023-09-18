def solution(n, stations, w):
    answer = 0
    curr = 0
    
    for s in stations:
        while curr < s-w-1:
            answer +=1
            curr += 1+2*w
        curr = s + w
        
    while curr<n:
        answer+=1
        curr +=1+2*w

    return answer