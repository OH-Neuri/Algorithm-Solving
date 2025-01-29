function solution(s) {
    return s
        .match(/\{(\d+,)*\d+\}/g)
        .map(set => set.slice(1, -1).split(',').map(Number))
        .sort((a, b) => a.length - b.length)
        .map((cur, index, arr) => index ? cur.find(elem => !arr[index - 1].includes(elem)) : cur[0]);
}