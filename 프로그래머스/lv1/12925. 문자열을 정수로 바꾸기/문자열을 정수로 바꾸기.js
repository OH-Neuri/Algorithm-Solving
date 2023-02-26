function solution(s) {
    var answer =0;
   if(typeof(s)=='string'){
       answer= Number(s);
    }else{
       answer= s+"";
    }
    return answer;
}