function solution(msg) {
    let map = new Map();
    let answer = [];
    let index = 27;
    let w = "";
    let c = "";
    let temp = 0;
    
    for(let i = 0; i < msg.length; i++){
        w = msg[i];
        c = msg[i+1];
       if(!map.get(w+c)){
           map.set(w+c,index++);
           answer.push(w.charCodeAt()-64);
       }else{
           while(map.get(w+c)){
               temp = w+c;
               w = w+c;
               c = msg[++i+1];
           }
           map.set(w+c,index++);
           answer.push(map.get(temp));
       }
    }
    return answer;
}