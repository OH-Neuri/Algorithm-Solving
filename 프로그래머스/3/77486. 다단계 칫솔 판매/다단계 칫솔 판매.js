function solution(enroll, referral, seller, amount) {
    // 추천인 저장 
    let rdName = new Map()
    // 각 판매원이 득한 이익금
    let money = new Map()
    
    for(let i = 0;i<enroll.length;i++){
        rdName.set(enroll[i],referral[i])
        money.set(enroll[i],0)
    }

    // 이익 분배
    const distribute = (name,value) => {
        if(value<1) return 
        
        let dMoney = value - Math.floor(value*0.1)
        money.set(name, money.get(name) + dMoney )
        
        let nextName = rdName.get(name)
        if(nextName!=="-") distribute(nextName, value - dMoney)
    }
    
    for(let i=0;i<seller.length;i++){
        distribute(seller[i], amount[i]*100)    
    }
    
    // result 저장
    var answer = [];
    for(let i=0; i<enroll.length;i++){
        answer.push(money.get(enroll[i]))
    }
    return answer;
}