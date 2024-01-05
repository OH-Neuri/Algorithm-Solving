import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    q_pro = deque()
    q_pro.extend(progresses)
    q_spd = deque()
    q_spd.extend(speeds)
    
    while q_pro:
        l = len(q_pro)
        cnt = 1
        first = q_pro.popleft()
        sp = q_spd.popleft()
        days=1
        if first <100:
            days = math.ceil((100-first)/sp)
        
        for i in range(l-1):
            curr = q_pro.popleft()
            sp = q_spd.popleft()
            q_pro.append(curr+(sp*days))
            q_spd.append(sp)
            
        for i in range(l-1):
            curr = q_pro.popleft()
            sp = q_spd.popleft()
            if curr>=100:
                cnt +=1
            else:
                q_pro.appendleft(curr)
                q_spd.appendleft(sp)
                break
        answer.append(cnt)
    
    return answer

