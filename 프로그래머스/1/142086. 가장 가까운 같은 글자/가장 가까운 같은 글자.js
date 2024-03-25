function solution(s) {
    var answer = [];
    for(let i=s.length-1;i>=0;i--){
        let str = s[i]
        let cnt = 0
        for(let j=i;j>=0;j--){
            if(i==j) continue
            cnt+=1
            if(str==s[j]){
                answer.push(cnt)
                break
            }
            if(j==0) {answer.push(-1)}
        }
    }
    answer.reverse()
    answer.splice(0,0,-1)
    return answer;
}