N = int(input())
sequence = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1,N):
    min = 0
    for j in range(i):
        #나보다 큰 값들 중에서
        if sequence[j] > sequence[i]:
            # 제일 긴 수열을 찾아
            if dp[j] > min:
                min = dp[j]
        # 길이 1 증가해서 저장
        dp[i] = min + 1

print(max(dp))