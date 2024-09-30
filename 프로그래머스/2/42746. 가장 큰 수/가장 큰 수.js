function solution(numbers) {
  // number의 요소를 string화
  const numbersString = numbers.map((num) => String(num));
  // 정렬하기
  numbersString.sort((a, b) => {
    // b + a숫자와 a + b 숫자를 비교해서 내림차순으로 정렬
    return parseInt(b + a) - parseInt(a + b);
  })
  // 만들어진 배열 문자열화
  const answer = numbersString.join('');
  return answer[0] === '0' ? '0' : answer;
}