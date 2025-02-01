function solution(x, y, n) {
    var answer = 0;
    var que = [[y, 0]];
    while(que.length) {
        const [num, i] = que.shift();
        if(num === x) return i;
        if(num%2 === 0 && num/2 >= x) que.push([num/2, i+1]);
        if(num%3 === 0 && num/3 >= x) que.push([num/3, i+1]);
        if(num-n >= x) que.push([num-n, i+1]);
    }
    return -1;
}