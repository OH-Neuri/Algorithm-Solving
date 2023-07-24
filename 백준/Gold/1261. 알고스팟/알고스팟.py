from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = []

for i in range(M):
    graph.append(list(map(int, input()[:-1])))

dist = [[-1] * N for _ in range(M)]  # 벽을 깬 횟수를 저장

dx = [1, 0, -1, 0]  # 행이동
dy = [0, 1, 0, -1]  # 열이동


def bfs(a, b):
    queue = deque()
    queue.append([a, b]) #초기 0,0 값을 큐에 넣는다.
    dist[0][0] = 0  # 첫번째 벽을 깬 횟수는 0으로 초기화

    while queue:
        x, y = queue.popleft() #큐에 있는 값을 왼쪽부터 뺀다.
        for i in range(4):
            nx = x + dx[i]  # 행 이동
            ny = y + dy[i]  # 열 이동

            if nx < 0 or nx >= M or ny < 0 or ny >= N:  # 범위를 벗어나면 아래의 코드를 실행하지 않는다.
                continue

            if dist[nx][ny] == -1:  # 아직 해당 방을 방문하지 않았다면
                # 만약 벽이 없다면
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]  # 전의 벽을 깬 횟수 그대로 전달해준다.
                    queue.appendleft([nx, ny])  # 벽이 없는 곳을 우선적으로 돌도록 큐의 맨 왼쪽에 넣어준다

                # 만약 벽이 있다면
                else:
                    dist[nx][ny] = dist[x][y] + 1  # 전의 벽을 깬 횟수에서 +1 해준다.
                    queue.append([nx, ny])  # 큐의 맨 오른쪽에 추가


bfs(0, 0)
print(dist[M - 1][N - 1])