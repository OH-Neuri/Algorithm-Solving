from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
visited = dict()

def BFS():
    q = deque()
    q.append(N)
    visited[N] = N
    while q:
        n = q.popleft()
        if n == K:
            return n

        for x in n+1, n-1, n*2:
            if 0<=x<=100000 and x not in visited:
                if x > n > K: continue
                visited[x] = n
                q.append(x)


c = BFS()
answer = deque()
time = 0
while visited[c] != c:
    answer.appendleft(c)
    c = visited[c]
    time += 1
answer.appendleft(c)
print(time)
print(*answer)
