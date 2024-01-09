def solution(triangle):
    answer = 0
    l = len(triangle)
    dp = [[] for _ in range(l)]
    dp[0].append(triangle[0][0])
    
    for i in range(1, l):
        for j in range(i+1):
            # 왼쪽
            if j == 0:
                dp[i].append(dp[i-1][0] + triangle[i][j])
            # 오른쪽
            elif j == i:
                dp[i].append(dp[i-1][j-1] + triangle[i][j])
            
            # 가운데
            else:
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    
    return max(dp[l-1])