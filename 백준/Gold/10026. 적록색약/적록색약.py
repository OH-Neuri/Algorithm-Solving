from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]

dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]
q = deque()


def bfs(x, y):
    q.append((x, y))
    v[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            # 범위에 맞고, 방문 안했을 경우
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == False:
                if graph[nx][ny] == graph[x][y]:
                    v[nx][ny] = True  # 방문 표시
                    q.append((nx, ny))



x = 0
v = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if v[i][j] == False:
            bfs(i, j)
            x += 1

o = 0
v = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G': graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if v[i][j] == False:
            bfs(i, j)
            o += 1

print(x, o)