N = int(input())
sequence = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0]=1
if N > 0:
    for i in range(1,N):
        maxSequence = 0
        maxDp = 0
        for j in range(i):
            # 나보다 작으면서
            if sequence[i] > sequence[j]:
                # 작은 값들 중 dp값이 가장 큰 걸 찾아
                if dp[j] > maxDp:
                    maxDp = dp[j]
        # 1을 더해준다
        dp[i] = maxDp+1
print(max(dp))

