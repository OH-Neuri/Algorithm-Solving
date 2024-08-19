/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function (n) {
    if (n == 1) return 0
    if (n == 3) return 3
    if (n % 2 !== 0) return n + 1
    
    let result = solution(n)
    let answer = 0
    for (let [key, value] of result) {
        answer += (key*value)
    } 
    return answer 
}
 function solution(n) {
  let numCnt= new Map()
  for (var i = 2; i <= n; i++) {
    while (n % i === 0) {
      numCnt.set(i, (numCnt.get(i)||0)+1)
      n = n / i;
    }
  }
  return numCnt
}
  