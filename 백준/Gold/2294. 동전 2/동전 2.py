import sys
input = sys.stdin.readline

n, k = map(int,input().split())
dp = [float('inf') for _ in range(k+1)]
dp[0] =0
for i in range(n):
    v = int(input())
    for j in range(v,k+1):
        if dp[j-v] != float('inf'):
            dp[j] =min(dp[j-v]+1,dp[j])
if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)
