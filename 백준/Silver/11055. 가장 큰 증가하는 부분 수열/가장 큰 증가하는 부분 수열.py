N = int(input())
sequence = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = sequence[0]

for i in range(1,N):
    maxSum = 0
    for j in range(i):
        #나보다 작은 것들 중에서
        if sequence[j] < sequence[i]:
            #누적합이 가장 큰 것을 찾아
            if dp[j] > maxSum:
                maxSum = dp[j]
        #현재값과 합하여 저장
        dp[i] = maxSum + sequence[i]
print(max(dp))
