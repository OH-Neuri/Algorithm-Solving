function solution(order) {
  let result = 0;
  const stack = [];

  for (let i = 1; i <= order.length; i++) {
    stack.push(i);

    // 스택의 상자 번호가 주어진 순서와 일치하는지 확인
    while (stack.length !== 0 && stack.at(-1) === order[result]) {
      stack.pop(); // 일치하는 상자 번호는 스택에서 제거
      result++;
    }
  }

  return result;
}