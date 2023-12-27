from collections import deque
import sys
input = sys.stdin.readline


N, Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    s, e, v = map(int,input().split())
    graph[s].append((e,v))
    graph[e].append((s,v))

def BFS(node):
    answer = 0
    q = deque()
    q.append(node)
    visited[node] = True
    while q :
        curr = q.popleft()

        for next, usado in graph[curr]:
            if not visited[next] and usado >= K:
                answer += 1
                visited[next] = True
                q.append(next)
    return answer

for _ in range(Q):
    K, start = map(int,input().split())
    visited = [False] * (N + 1)
    print(BFS(start))