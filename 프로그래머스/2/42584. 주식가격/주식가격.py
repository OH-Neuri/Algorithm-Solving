from collections import deque
def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        curr = q.popleft()
        time = 0
        for t in q:
            time +=1
            if curr > t:
                break
        answer.append(time)
    return answer