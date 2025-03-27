function solution(keymap, targets) {
    var answer = [];
    const alpMinClick = Array.from({length:26}, () => Infinity)
    
    // 각 알파벳 키 최소 횟수 구하기
    for(let i = 0; i < keymap.length; i++){
        [...keymap[i]].forEach((v,j) => {
            const alpIdx = v.charCodeAt(0) - 65
            alpMinClick[alpIdx] = Math.min(alpMinClick[alpIdx], j + 1)
        })
    }
    
    // 클릭
    for(let i = 0; i < targets.length; i++){
        let click = 0
        let flag = false
        for(let char of targets[i]){
            const charIdx = char.charCodeAt(0) - 65
            if(alpMinClick[charIdx] == Infinity){
                flag = true
                break;
            }
            click += alpMinClick[charIdx]
        }
        if(flag){
            answer.push(-1)
        }else{
            answer.push(click)
        }
    }
    
    return answer;
}