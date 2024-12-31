function solution(s) {
    let answer = 0;
    let stack = [];
    let isCorrect = true;
  
    if (s.length % 2 === 1) return 0;   //주어진 문자열이 홀수인 경우에는 바로 0을 리턴
    
    for(let i=0; i<s.length; i++){       
       let str = s.slice(i) + s.slice(0,i);   //문자열을 왼쪽으로 1칸씩 회전
       isCorrect = true;
      
        for(let n of str){
            if(n === "[" || n === "{" || n === "(" ){
                stack.push(n);   //[ or { or ( 이면 stack으로 push
            }else{
                let opening = stack.pop();   //stack에 쌓여있는 요소중 마지막
                //↓ 짝이 맞으면 continue
                if (opening === "(" && n === ")") continue;
                if (opening === "{" && n === "}") continue;
                if (opening === "[" && n === "]") continue;
                //↓ 짝이 맞지 않으면 실패, isCorrect를 false로 만들고 break
              	isCorrect = false;
                break;
            };
        };
      
        //짝이 맞는다면 성공이므로 isCorrect는 true, answer에 +1씩 더하기
        if (isCorrect) answer++;
    };
    return answer;
};