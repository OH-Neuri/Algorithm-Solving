from collections import deque
def solution(queue1, queue2):
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    # 합이 홀수일 경우
    
    if (sum1+sum2) % 2 != 0:
        return -1
    
    while sum1 != sum2:  
        if sum1>sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            sum2 -= tmp
            sum1 +=tmp
        cnt += 1
        
        if sum1==0 or sum2==0 or cnt>len(queue1)*3:
            cnt = -1
            break
            
    return cnt
