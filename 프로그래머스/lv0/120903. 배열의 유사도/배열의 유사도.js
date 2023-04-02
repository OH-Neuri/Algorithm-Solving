function solution(s1, s2) {
    let cnt=0;
    for(let i=0;i<s1.length;i++){
        for(let j=0;j<s2.length;j++){
            if(s1[i]==s2[j]) cnt++;
        }
    }

    return cnt;
}