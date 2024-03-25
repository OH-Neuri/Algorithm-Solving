function solution(cards1, cards2, goal) {
    for(let i=0;i<goal.length;i++){
        if(cards1[0]==goal[i]){
            cards1.splice(0,1)
        }else if (cards2[0]==goal[i]){
            cards2.splice(0,1)
        }else{
            return "No"
        }
    }
    return "Yes";
    
}