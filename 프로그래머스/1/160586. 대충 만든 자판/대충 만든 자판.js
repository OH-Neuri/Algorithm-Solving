function solution(keymap, targets) {
    let hash = {}
    var answer = [];
    targets.forEach(t=>{
        let sum = 0 
        for(let i=0;i<t.length;i++){
            let min = Infinity
            for(let j=0; j<keymap.length; j++){
                let index = keymap[j].indexOf(t[i])
                if(min >index && index!=-1) min = index
            }
            if(min==Infinity){
                sum = -1
                break
            }
            else {
                sum += min+1
            }
        }
        answer.push(sum)
    })
    return answer;
}