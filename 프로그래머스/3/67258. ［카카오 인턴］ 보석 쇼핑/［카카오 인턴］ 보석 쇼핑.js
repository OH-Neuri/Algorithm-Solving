function solution(gems) {
    var answer = [0, gems.length-1];
    let gemKinds = new Set(gems).size
    let gemMap = new Map()
    
    let start = 0
    for(let end = 0; end < gems.length; end++){
        
        // 보석 넣기
        gemMap.set(gems[end], (gemMap.get(gems[end])||0) + 1)
        
        // 종류가 다 있는 경우
        while(gemMap.size == gemKinds){
            
            // 최소 갱신
            if(end - start < answer[1] - answer[0]){
                answer = [start, end]
            }
            
            gemMap.set(gems[start],(gemMap.get(gems[start]) - 1 ))
            if(gemMap.get(gems[start])===0) gemMap.delete(gems[start])
            start++;
        }
    }
    return [answer[0]+1, answer[1]+1]
}