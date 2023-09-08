from collections import deque
def solution(x, y, n):
    visited = [-1] *1000001
    q = deque([x])
    while q:
        curr = q.popleft()
        if curr == y:
            return visited[curr] +1
    
        for a in (curr+n),(curr*2),(curr*3):
            if a<1000001 and visited[a] == -1:
                visited[a] = visited[curr]+1
                q.append(a)    

    return visited[y]