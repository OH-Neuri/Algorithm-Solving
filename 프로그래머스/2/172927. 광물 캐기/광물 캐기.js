function solution(picks, minerals) {
    var answer = 0;
    let count = 0 // 5개 묶음 카운트
    let groups = 0 // 5개씩 묶음 값
    let fatigue = 0 // 피로도 
    let dPck = picks[0]
    let iPck= picks[1]
    let sPck = picks[2]
    const sortedMineralGroups = []
    
    // 곡괭이 부족해서 캘 수 없는 광물 없애기
    const len = dPck * 5 + iPck * 5 + sPck * 5
    minerals.splice(len)

    for(let i = 0; i < minerals.length; i++){
        let tmp = 0 
        if(minerals[i] === "diamond") tmp = 100;
        if(minerals[i] === "iron") tmp = 10;
        if(minerals[i] === "stone") tmp = 1;
        
        groups += tmp;
        count++;
        
        if(count === 5){
            sortedMineralGroups.push(groups)
            groups = 0
            count = 0
        }
    }
    
    if(count) sortedMineralGroups.push(groups)
    sortedMineralGroups.sort((a, b) => b - a)
    

    let idx = 0
    
   
    
    while((dPck !==0 || iPck!==0 || sPck!==0)  && idx < sortedMineralGroups.length){
        const currMineral = sortedMineralGroups[idx]
        const diaCnt = Math.floor(currMineral/100);
        const ironCnt = Math.floor((currMineral%100) / 10);
        const stoneCnt = currMineral % 10;
        idx++;
        if(dPck !== 0){
            fatigue += diaCnt + ironCnt + stoneCnt
            dPck--;
            continue;
        }
        
        if(iPck !== 0){
            fatigue += diaCnt * 5 + ironCnt + stoneCnt
            iPck--;
            continue
        }
        
        if(sPck !== 0){
            fatigue += diaCnt * 25 + ironCnt * 5 + stoneCnt
            sPck--;
        }
    }
    
    return fatigue;
}

