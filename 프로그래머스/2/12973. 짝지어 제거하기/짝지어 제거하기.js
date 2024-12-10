function solution(s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const curr = s.charAt(i);
    if (stack[stack.length - 1] === curr) {
      stack.pop();
    } else {
      stack.push(curr);
    }
  }

  return stack.length === 0 ? 1 : 0;
}