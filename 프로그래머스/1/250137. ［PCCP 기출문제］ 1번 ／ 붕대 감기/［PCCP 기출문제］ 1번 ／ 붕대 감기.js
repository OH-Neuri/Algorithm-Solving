function solution(bandage, health, attacks) {

    let len = attacks.length
    const lastAttackTime = attacks[len-1][0]
    const hpLog = Array.from({length:lastAttackTime + 1}, () => 0)
    
    let currHealth = health // 현재 체력
    let attackIdx = 0 // 공격 순서
    let healthCnt = 0 // 회복 카운트
    
    for(let time = 1; time <= lastAttackTime; time++){

        // 공격 X
        if(time!==attacks[attackIdx][0]){
            currHealth+=bandage[1] // 1초 회복
            healthCnt++;
            if(healthCnt===bandage[0]) {
                currHealth+=bandage[2]
                healthCnt=0
            }
            if(currHealth>health) currHealth = health 
        }else{   
        // 공격 O
            currHealth = currHealth - attacks[attackIdx][1]
            if(currHealth<=0) return -1
            attackIdx++;
            healthCnt=0;
        }
    }

    return currHealth;
}