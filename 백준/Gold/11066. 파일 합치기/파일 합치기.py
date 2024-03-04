import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    matrix = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    s = 0
    summ = [0]
    for i in range(N):
        s += matrix[i]
        summ.append(s)

    for diff in range(1,N):
        for start in range(N-diff):
            end = start + diff
            cost = summ[end+1] - summ[start]
            dp[start][end] = 1e9
            for mid in range(start,end):
                dp[start][end] = min(dp[start][end], cost + dp[start][mid] + dp[mid+1][end])
    print(dp[0][N-1])

