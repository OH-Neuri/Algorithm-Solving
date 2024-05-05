function solution(want, number, discount) {
    var answer = 0;
    
    for(let i=0; i<discount.length; i++) {
       
        if(check(want, number, discount.slice(i, i+10))) answer++;
    }
    return answer;
}
function check(want, number, discount) {

    const map = new Map();
    
    for(let i=0; i<discount.length; i++) {
    
        map.has(discount[i]) ? map.set(discount[i], map.get(discount[i])+1) : map.set(discount[i], 1);
    }
    
    for(let i=0; i<want.length; i++) {
        if(isNaN(map.get(want[i]))) return false;
        if(number[i] > map.get(want[i])) return false;
    }
    return true;
}