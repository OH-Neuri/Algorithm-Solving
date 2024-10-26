function solution(n, k) {
    const answer = [];
    const people = Array.from({ length: n }, (_, i) => i + 1);
    let caseNum = people.reduce((ac, v) => ac * v, 1)
    
    while (answer.length < n) {
        caseNum = caseNum / people.length;
        answer.push(...people.splice(Math.floor((k - 1) / caseNum), 1));
        k = k % caseNum;
    }

    return answer;
}