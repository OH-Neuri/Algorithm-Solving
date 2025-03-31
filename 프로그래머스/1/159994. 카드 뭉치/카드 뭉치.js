function solution(cards1, cards2, goal) {
    var answer = "Yes";
    let cd1Idx = 0
    let cd2Idx = 0
    
    for(let word of goal){
        if(cards1[cd1Idx]===word){
            cd1Idx++;
        }else if(cards2[cd2Idx]===word){
            cd2Idx++;
        }else{
            answer = "No"
            break
        }
    }
    return answer;
}