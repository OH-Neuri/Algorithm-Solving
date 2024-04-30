function solution(begin, target, words) {
    let visited = Array.from({length:words.length},()=>[Infinity])
    let wordListLength = words.length
    let wordLength = words[0].length
    words = words.map(v=>v.split(""))
    let queue = [[begin.split(""),1]]
    
    // BFS
    while(queue.length){
        let current = queue.shift()
        let cw = current[0]
        let cnt = current[1]
        
        if(cw.join("") === target) return cnt-1
        
        for(let i=0;i<wordListLength;i++){
            let checkOneWord = 0
            for(let j=0; j<wordLength;j++){
                if(cw[j]!==words[i][j]) {
                    if(checkOneWord>1) {break}
                    checkOneWord +=1
                }
            }
            if(checkOneWord <=1 && cnt < visited[i]){
                visited[i] = cnt
                queue.push([words[i],cnt+1])
            }
        }
    }
    return 0;
}