function solution(today, terms, privacies) {
    var answer = [];
    let termsHash = {}
    let currentTime = today.split('.').map(i=>Number(i))
    currentTime = currentTime[0]*336 + currentTime[1]*28 + currentTime[2]
    for(let i=0;i<terms.length;i++){
        let tmp = terms[i].split(" ")
        termsHash[tmp[0]] = Number(tmp[1])
    }
    
    for(let i=0;i<privacies.length;i++){
        let term = privacies[i].split('').pop()
        let date = privacies[i].slice(0,-1).split('.').map(i=>Number(i))
        let period = date[0]*336+date[1]*28+date[2] +(termsHash[term]*28) 
        if(currentTime>=period) answer.push(i+1)
    }
    return answer;
    
}