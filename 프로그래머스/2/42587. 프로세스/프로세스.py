from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i, v in enumerate(priorities):
        if i==location:
            q.append((v,1))
        else:
            q.append((v,0))
    
    if len(q) == 1:
        return 1
    
    while q:
        max_value = max(q)[0]
        curr, l = q.popleft()
        # 우선순위가 가장 높은 경우
        if curr == max_value:
            # 우선순위 갱신
            if q:
                max_value = max(q)[0]
            answer += 1
            if l == 1:
                break
        else:
            q.append((curr,l))
        
    return answer

 