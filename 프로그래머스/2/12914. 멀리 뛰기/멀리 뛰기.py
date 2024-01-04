def solution(n):
    answer = 0
    dp = [0 for _ in range(2010)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    
    if n > 4:
        for i in range(4,n+1):
            dp[i] = dp[i-1]%1234567 + dp[i-2]%1234567

    return dp[n]%1234567

