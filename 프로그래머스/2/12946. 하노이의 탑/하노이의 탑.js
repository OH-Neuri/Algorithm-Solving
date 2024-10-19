function solution(n) {
  let answer = [];
  
  const hanoi = (n, start, mid, end) => {
    if (n === 1) answer.push([start,end])
    else {
      hanoi(n-1, start, end, mid)
      answer.push([start,end])
      hanoi(n-1, mid, start, end)
    }
  }
  
  hanoi(n, 1, 2, 3)
  return answer
}