import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    W, V = map(int, input().split())
    for j in range(K + 1):
        if j >= W:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - W] + V) # 이전에 넣었던 짐에서 현재 짐 넣어보기
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])
