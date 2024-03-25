function solution(answers) {
    let p = [0,0,0]
    let rule1 = [1,2,3,4,5]
    let rule2 = [2,1,2,3,2,4,2,5]
    let rule3 = [3,3,1,1,2,2,4,4,5,5]
    
    for(let i=0;i<answers.length;i++){

        if(answers[i]==rule1[i%rule1.length]){
            p[0] +=1
        }
        if(answers[i]==rule2[i%rule2.length]){
            p[1] +=1
        }
        if(answers[i]==rule3[i%rule3.length]){
            p[2] +=1
        }        
    }
    let answer = []
    let max = Math.max.apply(null,p)
    
    for(let i=0; i<3;i++){
        if(p[i]==max)
            answer.push(i+1)
    }
    
    return answer;
}