function solution(info, n, m) {
    let dp = Array.from({length:info.length+1}, ()=>Array(m).fill(Infinity))
    
    dp[0][0] = 0;
    
    for(let i = 1; i <= info.length; i++){
        let [a, b] = info[i-1];
        
        for(let j = 0;j < m; j++){
            // A도둑이 현재 물건을 훔치는 경우
            dp[i][j] = Math.min(dp[i-1][j] + a, dp[i][j])
            
            // B도둑이 현재 물건을 훔치는 경우 
            if(j + b <m){
                dp[i][j+b] = Math.min(dp[i-1][j], dp[i][j+b])
            }
        }
    }
    
    let min = Infinity;
    
    console.log(dp)
    dp[info.length].forEach((v)=>{
        if(v<n){
            min = Math.min(min,v)
        }
    })    
    
    return min === Infinity ? -1 : min
}