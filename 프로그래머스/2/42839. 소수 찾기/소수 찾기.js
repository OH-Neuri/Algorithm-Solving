function solution(numbers) {
    return [...new Set(getPer(numbers))].filter(v => isPrime(v)).length;
}

const getPer = (str) => {
    const answer = [];
    const n = str.length;
    let ch = Array.from({ length: n }, () => 0);
    
    const dfs = (curStr) => {
        answer.push(+curStr);
        for (let i = 0; i < n; i++) {
            if (ch[i] === 0) {
                ch[i] = 1;
                dfs(curStr + str[i]);
                ch[i] = 0;
            }
        }
    }
    dfs('');
    answer.shift();
    return answer;
}

const isPrime = (n) => {
    if (n === 0 || n === 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}