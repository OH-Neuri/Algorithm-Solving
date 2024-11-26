function solution(targets) {
    targets.sort((a,b) => a[1] - b[1])
    let count = 0
    for (let i = 0; i < targets.length; i ++) {
        let endPoint = targets[i][1]
        while (i < targets.length - 1 && targets[i + 1][0] < endPoint) {
            i ++                        
        }
        count ++
    }
    
    return count
}