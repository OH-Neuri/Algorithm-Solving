function solution(number, k) {
  let stack = [];

  for (let i = 0; i < number.length; i++) {
    const element = number[i];
    // stack 마지막 숫자와 현재 숫자를 비교하여 현재 숫자가 더 크면 stack의 마지막 숫자 pop
    while (k > 0 && stack[stack.length - 1] < element) {
      stack.pop();
      k--;
    }
    stack.push(element);
  }

  // 모든 숫자 비교가 끝난 후, k가 0보다 크다면 남은 k만큼 뒤에서 제거
  stack.splice(stack.length - k, k);
  return stack.join("");
}