function solution(matrix_sizes) {
    let answer = 0
    
    const matrixLength = matrix_sizes.length
    const arr = Array(matrixLength+1)
    
    arr[0] = matrix_sizes[0][0]
    for(let i = 1; i < matrixLength + 1; i++) {
        arr[i] = matrix_sizes[i-1][1] 
    }
    
    const dp = Array(matrixLength).fill(0).map(_=>[...new Array(matrixLength+1).fill(-1)])
    
    const getMin = (start, end) => {
        if(dp[start][end] !== -1) {
            return dp[start][end]
        }
        if(end-start === 1) {
            dp[start][end] = 0
        } else if(end-start === 2) {
            dp[start][end] = arr[start] * arr[start+1] * arr[start+2]
        } else {
            let min = Infinity
            for(let i = 1; i < end - start; i++) {
                let value = getMin(start, start+i) + getMin(start+i, end) + arr[start] * arr[start+i] * arr[end]
                if(min > value) min = value
            }
            dp[start][end] = min
        }
        return dp[start][end]
    }

    
    return getMin(0, matrixLength);
}