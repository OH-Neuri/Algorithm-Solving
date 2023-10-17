from collections import deque
def solution(plans):
    
    answer = []
    for i in range(len(plans)):
        plans[i][1] = int(plans[i][1][:2])*60 + int(plans[i][1][3:])
        plans[i][2] = plans[i][1] + int(plans[i][2]) 
    plans = sorted(plans, key=lambda x:x[1])
    
    stack = []
    a = deque(plans)
    stack = []
    
    while a:
        if len(a) >= 2 and a[0][2] > a[1][1]:
            x, y, z = a.popleft()
            stack.append([x, z- a[0][1]])

        else:
            x, y, z = a.popleft()
            answer.append(x)
            
            if stack:
                i, j = stack.pop()
                a.appendleft([i, z, z + j])
                
    return answer
