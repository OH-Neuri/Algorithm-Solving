function solution(X, Y) {
    var answer = -1;
    let friend = ""
    for(let i = 0; i < 10; i++){
        const numStr = i.toString()
        if(X.includes(numStr) && Y.includes(numStr)){
            const cnt = Math.min(X.split(numStr).length - 1,
                                 Y.split(numStr).length - 1)
            friend += numStr.repeat(cnt)
        }
    }
    
    if(!friend) return "-1"
    if(!Number(friend)) return "0" 
    
    answer = friend.split("").sort((a, b)=> b - a).join("")
    return answer;
}