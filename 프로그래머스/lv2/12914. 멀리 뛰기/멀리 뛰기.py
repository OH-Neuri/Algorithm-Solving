def solution(n):
    dp = [0]*2001
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i] = dp[i-1]%1234567 + dp[i-2]%1234567
        
    return dp[n]%1234567