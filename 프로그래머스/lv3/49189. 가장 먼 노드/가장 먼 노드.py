from collections import deque
def solution(n, vertex):
    
    node = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for a, b in vertex:
        node[a].append(b)
        node[b].append(a)
        
    visited[1]=1
    q = deque([1])
    
    while q:
        curr = q.popleft()
        for next in node[curr]:
            if not visited[next]:
                visited[next] = visited[curr]+1
                q.append(next)
    
    max_v = max(visited)
    cnt = visited.count(max_v)
        
    return cnt if cnt >0 else 1