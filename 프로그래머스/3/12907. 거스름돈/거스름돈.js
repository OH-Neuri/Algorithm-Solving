function solution(n, money) {
    var answer = 0;
    let dp = Array.from({length:n+1}, ()=>0)
    dp[0] = 1
    
    for(let coin of money){
        for(let i=0; i<n+1;i++){
            if(i-coin>=0){
              dp[i] = (dp[i] + dp[i-coin]) %1000000007       
            }
        }
    }
    return dp[n];
}
