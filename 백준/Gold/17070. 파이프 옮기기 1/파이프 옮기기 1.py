import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def DFS(i, j, d):
    global N, answer
    if i == N - 1 and j == N - 1:
        answer += 1
        return

    if d == 1 or d == 3:
        if j + 1 < N and arr[i][j + 1] != 1:
            DFS(i, j + 1, 1)
    if d == 2 or d == 3:
        if i + 1 < N and arr[i + 1][j] != 1:
            DFS(i + 1, j, 2)

    if i + 1 < N and j + 1 < N:
        if arr[i + 1][j] != 1 and arr[i][j + 1] != 1 and arr[i + 1][j + 1] != 1:
            DFS(i + 1, j + 1, 3)

if arr[N-1][N-1] == 1:
    print(0)
else:
    DFS(0, 1, 1)
    print(answer)
