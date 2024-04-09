from collections import deque
def solution(n, m, section):
    q = deque(section)
    first = q.popleft()
    answer = 1
    while q:
        c = q.popleft()
        if first+m >c:
            continue
        else:
            first = c
            answer +=1
    return answer