
function solution(today, terms, privacies) {
    var answer = [];
    const dayOfToday = dateToDay(today) // 오늘 날짜
    const daysOfTerms = new Map // 약관 날짜
    for(let i = 0; i<terms.length; i++){
        const termsArr = terms[i].split(" ")
        daysOfTerms.set(termsArr[0], termsArr[1]*28)
    }
    
    for(let i = 0; i < privacies.length; i++){
        const privaciesArr = privacies[i].split(" ")
        const dayOfPrivacies = dateToDay(privaciesArr[0]) // 날짜를 일 수로 변환
        const dayOfTerms = daysOfTerms.get(privaciesArr[1]) // 약관종류 일 수로 변환
        
        if(dayOfPrivacies + dayOfTerms <= dayOfToday) answer.push(i+1)
    }
    
    return answer;
}

function dateToDay(date){
    const dateArr = date.split(".")
    const year = Number(dateArr[0])
    const month = Number(dateArr[1])
    const day = Number(dateArr[2])
    
    return (year-2000)*336 + (month*28) + day
}