function solution(weights) {
    var answer = 0;
    const ratios = [
        [1,1],
        [3,2],
        [4,3],
        [2,1],
        [2,3],
        [3,4],
        [1,2],
    ]
    
    const countMap = new Map()
    for(let w of weights){
        for(const [a, b] of ratios){
            const target = (w * a) / b;
            if(Number.isInteger(target) && countMap.has(target)){
                answer += countMap.get(target)
            }
        }
        
        countMap.set(w, (countMap.get(w) ??  0) + 1)
    }
    
    return answer;
}

  // const countMap = new Map()
    // 몸무게별 인원수 저장
//     for(let weight of weights){
//         countMap.set(weight, (countMap.get(weight) || 0) + 1)
//     }
    
    // 100, 100, 100, 100, 100 -> 10
    // 100, 100, 100, 100 -> 6
    // 100, 100, 100 -> 3
    // n(n-1)/2
    // 같은 사람 몸무게 먼저 쌍찾기
//     for(let [weight, cnt] of wMap.entries()){
//         if(cnt >= 2){
//             answer += cnt * (cnt-1) / 2 
//         }
