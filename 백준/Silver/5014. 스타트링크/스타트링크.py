from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int,input().split())
visited = [0] * 1000001
visited[S] = 1
q = deque([S])

def BFS():

    while q:
        curr = q.popleft()
        # G층에 도달하면 리턴
        if curr == G:
            return print(visited[curr]-1)
        up = curr + U
        # 건물
        if up <= F and visited[up] == 0:
            visited[up] = visited[curr] + 1
            q.append(up)
        down = curr - D
        if down >= 1 and visited[down] == 0:
            visited[down] = visited[curr] + 1
            q.append(down)
    return print("use the stairs")
BFS()



