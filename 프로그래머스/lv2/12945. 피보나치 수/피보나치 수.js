function solution(n) {
    var dp = Array(n+1)
    dp[0]=0
    dp[1]=1
    for(let i=2;i<dp.length;i++){
        dp[i] = (dp[i-1]+dp[i-2])%1234567
    }
    return dp[dp.length-1];
}