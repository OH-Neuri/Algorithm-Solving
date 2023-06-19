N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(2,N+1):
    # -1
    dp[i] = dp[i-1]+1
    # 3으로 나눈 경우
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    # 2로 나눈 경우
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])