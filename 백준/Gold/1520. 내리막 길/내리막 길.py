import sys
input = sys.stdin.readline

d = [(1,0),(0,1),(-1,0),(0,-1)]
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

def DFS(i,j):
    # 제일 오른쪽 아래 지점에 도착했을 경우,
    if i == N-1 and j == M-1:
        return 1

    # 이미 저장된 경로의 수가 있는 경우,
    if visited[i][j] >= 0:
        return visited[i][j]

    # 처음 방문한 경우
    visited[i][j] = 0

    for dx, dy, in d:
        nx, ny = i + dx, j + dy

        # 배열 범위 안에 있고 다음 경로 높이가 더 낮을 경우
        if 0<=nx<N and 0<=ny<M and arr[i][j] > arr[nx][ny]:
            visited[i][j] += DFS(nx,ny)

    return visited[i][j]

answer = DFS(0,0)
print(answer)