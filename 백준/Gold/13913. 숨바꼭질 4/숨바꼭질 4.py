from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = start
    while q:
        c = q.popleft() #current
        if c == k:
            return c
        for i in (c-1, c+1, 2*c):
            if 0 <= i <= 100000 and i not in visited:
                if i > c > k : continue
                visited[i] = c
                q.append(i)

n, k = map(int, input().split())
visited = dict()
c = bfs(n)
ans = deque()
cnt = 0
while visited[c] != c:
    ans.appendleft(c)
    c = visited[c]
    cnt += 1
ans.appendleft(c)
print(cnt)
print(*ans)