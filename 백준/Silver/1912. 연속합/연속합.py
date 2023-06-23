N = int(input())
sequence = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = sequence[0]

for i in range(1,N):
    # 이전 값과 현재 값을 더한 값이 현재 값보다 큰 경우
    if dp[i-1] + sequence[i] <= sequence[i]:
        dp[i] = sequence[i]
    else:
        dp[i] = dp[i-1] + sequence[i]
print(max(dp))