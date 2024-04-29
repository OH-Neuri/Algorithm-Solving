const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

function isSameArray(S,T){
    for(let i=0;i<T.length;i++){
        if(S[i]!==T[i]) return false
    }
    return true;
}

let S = input[0].trim().split("")
let T = input[1].trim().split("")
let answer = 0
while(1){
    if(S.length === T.length){
        if(isSameArray(S,T)) answer =1
        break;
    }
    if(T[T.length-1]==='A'){
        T.pop()
    }else{
        T.pop()
        T.reverse()
    }
}
console.log(answer)