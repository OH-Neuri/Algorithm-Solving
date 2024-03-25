function solution(keymap, targets) {
    const result = [];
    
    for (const target of targets) {
        let totalCnt = 0;
        
        const visited = {}; // 이미 방문한 문자 저장
        
        for (let i = 0; i < target.length; i++) {
            const char = target[i];
            
            if (visited[char] !== undefined) {
                totalCnt += visited[char];
                continue;
            }
            
            let minIndex = Infinity;
            
            for (const key of keymap) {
                const index = key.indexOf(char) + 1;
                if (index !== 0) {
                    minIndex = Math.min(minIndex, index);
                }
            }
            
            if (minIndex === Infinity) {
                totalCnt = -1;
                break;
            }
            
            visited[char] = minIndex;
            totalCnt += minIndex;
        }
        
        result.push(totalCnt);
    }
    
    return result;
}
