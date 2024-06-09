function solution(clothes) {
    let answer = 1;
    const obj = {};
    clothes.map(c => {
        if(obj[c[1]]){
            return obj[c[1]]+=1;
        }else{
            return obj[c[1]] = 1;
        }
    })
    const value = Object.values(obj);
    for(let i = 0; i < value.length; i++){
        answer *= value[i]+1;
    }
    return answer-1;
}