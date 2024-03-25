function solution(lottos, win_nums) {
    var answer = [];
    let maxCnt = 0
    let minCnt = 0
    let origin = lottos.filter((i)=>i!==0)
    
    for(lotto of origin){
        let index = win_nums.indexOf(lotto)
        if(index!==-1){
            win_nums.splice(index,1)
            minCnt+=1
        }
    }
    maxCnt = lottos.length - origin.length + minCnt
    maxCnt = convertValue(maxCnt)
    minCnt = convertValue(minCnt)
    
    return [maxCnt,minCnt];
}
function convertValue(v){
    switch(v){
        case 6:
            return 1;
        case 5:
            return 2;
        case 4:
            return 3;
        case 3:
            return 4;
        case 2:
            return 5;
        default:
            return 6;
    }
}