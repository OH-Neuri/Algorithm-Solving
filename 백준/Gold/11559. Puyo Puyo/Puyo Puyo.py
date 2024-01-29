from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
field = [list(map(str, input().rstrip())) for _ in range(12)]

# c : 색깔
# 터질 뿌요들 모아오기
def BFS(i, j, c):
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    e = [(i,j)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and field[nx][ny] == c:
                visited[nx][ny] = True
                q.append((nx,ny))
                e.append((nx,ny))
    if len(e) >=4:
        return e
    else:
        return []

# 터뜨린 다음 뿌요들 아래로 내리기
# e : 터질 뿌요들
def explode_puyo(e):
    # 터뜨리기
    for i in range(len(e)):
        field[e[i][0]][e[i][1]] = '.'
    for i in range(6):
        stack = []
        for j in range(11,-1,-1):
            if field[j][i] !='.':
                stack.append(field[j][i])
        stack = stack[::-1]
        for j in range(11,-1,-1):
            if stack:
                field[j][i] = stack.pop()
            else:
                field[j][i] = '.'

ep = 0
while True:
    ep_list = [] # 1연쇄에 터질 뿌요들
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                ep_list += BFS(i,j,field[i][j])
    if len(ep_list)>=4:
        explode_puyo(ep_list)
        ep += 1
    else:
        break

print(ep)