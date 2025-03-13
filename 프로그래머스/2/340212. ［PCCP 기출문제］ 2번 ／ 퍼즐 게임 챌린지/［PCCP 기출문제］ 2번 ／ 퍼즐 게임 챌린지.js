function solution(diffs, times, limit) {
  // 이분탐색 ㄱㄱㄱ
    let [left, right] = [1, diffs.reduce((acc, cur) => Math.max(acc, cur), 1)]
    let answer = -1;
    
    while(left<=right){
        // 레벨
        const mid = Math.floor((right+left)/2)
        let time = 0 
        
        for(let i = 0; i< diffs.length; i++){
            if(diffs[i]<=mid){
                time+= times[i];
            }else{
                time+= (diffs[i]-mid)*(times[i-1]+times[i]) + times[i] 
            }
            if(time>limit) break; // 제한 초과 시 중단
        }
        
        if(time<=limit){
            answer = mid
            right = mid-1
        }else{
            left = mid +1
        }
    }
    
    return answer
}

//     let minLevel = Infinity
    
//     for(let level = 1; level <= 100; level++){
//         let time = 0
        
//         for(let i = 0; i< diffs.length; i++){
//             if(diffs[i]<=level){
//                 time+= times[i];
//             }else{
//                 time+= (diffs[i]-level)*(times[i-1]+times[i]) + times[i] 
//             }
//             if(time>limit) break;
//         }
        
//         console.log(time)
//         if(time<=limit){
//             minLevel = Math.min(minLevel,level)
//         }
        
//     }
    
//     return minLevel === Infinity? -1: minLevel



