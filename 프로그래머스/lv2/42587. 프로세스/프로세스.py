from collections import deque

def solution(priorities, location):
    
    answer = 0
    queue = deque(priorities)
    
    while queue:
        m = max(queue)
        l = queue.popleft()
        location -=1
        # 우선순위 낮을경우
        if l != m:
            queue.append(l)
            if location <0:
                location = len(queue)-1
        # 우선순위일 경우
        else:
            answer+=1
            if location < 0:
                break
    return answer