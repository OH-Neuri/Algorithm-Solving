function solution(x) {
    return x%((x+"").split("").reduce((sum,curr,i)=>Number(sum)+Number(curr),0))==0?true:false;
}