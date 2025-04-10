function solution(begin, target, words) {
    var answer = 0;
    const len = begin.length
    
    // 변환할 수 없는 경우에는 0를 return한다.
    if(!words.includes(target)) return 0
    
    const queue = []
    queue.push([begin, [begin]]) // 비효율적인듯
    let start = 0
    while(start < queue.length){
        const [currWord, visitedWord] = queue[start++]
        
        if(currWord === target) return visitedWord.length - 1
        
        for(let word of words){
            // 이미 사용했던 단어는 패스
            if(visitedWord.includes(word)) continue
            
            // 한 번에 한 개의 알파벳만 바꿀 수 있다.
            let same = 0
            for(let i = 0; i < len; i++){
                if(currWord[i]===word[i]) same++
            }
            // 단어 하나만 다를 경우
            if(same === len - 1){
                const tmpArr = [...visitedWord]
                tmpArr.push(word)
                queue.push([word, tmpArr])
            }
        }
    }
}