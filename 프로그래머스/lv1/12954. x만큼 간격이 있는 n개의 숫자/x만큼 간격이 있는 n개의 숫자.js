function solution(x, n) {
    return (Array(n).fill(x).map((v, i) => (i + 1) * v))
}