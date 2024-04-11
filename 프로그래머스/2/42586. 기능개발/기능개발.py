from collections import deque
def solution(progresses, speeds):
    q = deque(progresses)
    s = deque(speeds)
    day = 1
    distribute = 0
    answer = []
    
    while q:
        c_q = q.popleft()
        c_s = s.popleft()
        
        if c_q + (c_s * day) < 100:
            if distribute:
                answer.append(distribute)
                distribute = 0
            while c_q + (c_s * day) <100:
                day+=1
            distribute = 1
        else:
            distribute +=1
        
    answer.append(distribute)
    
    return answer