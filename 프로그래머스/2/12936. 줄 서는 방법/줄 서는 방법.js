function solution (n, k) {
  const answer = [];
  const arr = new Array(n).fill(1);
  for(let i = 1; i < n; i++) arr[i] = arr[i-1] + 1;
  
  let nth = k-1;
  
  while(arr.length) {
    if(nth === 0) {
      answer.push(...arr);
      break;
    }
    
    const fact = factorial(arr.length - 1);
    const index = nth / fact >> 0;
    nth = nth % fact;
    
    answer.push(arr[index]);
    arr.splice(index, 1);
  }
  
  return answer;
}

const factorial = (n) => {
  let res = 1;
  for(let i = 2; i <= n; i++) res *= i;
  return res;
}