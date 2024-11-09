function solution(k, d) {
    var answer = 0;
    function yFun(x){
        return (Math.floor(Math.sqrt(d*d-x*x)));
    }
    
    for(var x = 0;x<=d;x+=k){
        answer+=((Math.floor(yFun(x)/k))+1);
    }
    return answer;
}