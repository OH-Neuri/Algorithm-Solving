function solution(triangle) {
    var answer = 0;
    let len = triangle.length
    let dp = Array.from({length:len},()=>[])
    for(let i=0;i<len;i++){
        for(let j=0;j<triangle[i].length;j++){
            dp[i].push(-1)
        }
    }
    
    function recur(i, j){
        if(i == len) return 0
        if(j<0 || j>=triangle[i].length) return -999999
        if(dp[i][j]!==-1) return dp[i][j]
        
        dp[i][j]= Math.max(recur(i+1,j), recur(i+1,j+1)) + triangle[i][j]
    
        return dp[i][j]
    }

    recur(0,0)
    return dp[0][0];
}


