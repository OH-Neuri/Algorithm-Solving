def solution(n):
    answer = 0
    idx = n//2
    dp = [0]*(idx+1)
    dp[0]=0
    dp[1]=3
    dp[2]=11
    
    if n%2!=0:
        return 0
    if n<3:
        return dp[n]
    
    for i in range(3, idx+1):
        dp[i] = (dp[i-1]*3 + sum(dp[1:i-1])*2+2)%1000000007
    return dp[idx]
    
