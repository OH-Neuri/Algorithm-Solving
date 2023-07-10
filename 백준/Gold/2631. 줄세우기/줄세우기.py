import sys
input = sys.stdin.readline
N = int(input())
children = []
dp = [0 for _ in range(N)]
dp[0] = 1
for _ in range(N):
    a = int(input())
    children.append(a)

for i in range(1, N):
    maxSum = 0
    for j in range(i):
        # 나보다 작으면서
        if children[j]<children[i]:
            # 최댓값을 찾자
            if maxSum<dp[j]:
                maxSum = dp[j]
    dp[i] = maxSum +1

print(N-max(dp))

