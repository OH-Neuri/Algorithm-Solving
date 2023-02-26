function solution(s){
    var answer = true;
    var sArr=(s+"").split("");
    let pCnt=0;
    let yCnt=0;
    for(let i=0;i<sArr.length;i++){
        if(sArr[i]=='p'||sArr[i]=='P'){
            pCnt++;
        }else if(sArr[i]=='y'||sArr[i]=='Y'){
            yCnt++;
        }
    }
    return answer= pCnt==yCnt?true:false;
}