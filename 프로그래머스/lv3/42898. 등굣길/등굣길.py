def solution(m, n, puddles):
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)] 

    for puddle in puddles:
        dp[puddle[1]][puddle[0]]=0

    check=False
    for i in range(1,n+1):
        if dp[i][1]==0: check=True

        if check: dp[i][1]=0
        else: dp[i][1]=1

    check=False 
    for i in range(1,m+1):
        if dp[1][i]==0: check=True

        if check: dp[1][i]=0
        else: dp[1][i]=1


    for i in range(2,n+1):
        for j in range(2,m+1):
            if dp[i][j]==0: continue
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]%1000000007