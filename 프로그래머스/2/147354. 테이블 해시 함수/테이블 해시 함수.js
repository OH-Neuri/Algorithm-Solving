function solution(data, col, row_begin, row_end) {
  let answer = 0;

  const sort_data = data.sort((a, b) => {
    if (a[col - 1] < b[col - 1]) {
      return a[col - 1] - b[col - 1];
    } else if (a[col - 1] === b[col - 1]) {
      return b[0] - a[0];
    }
  });

  for (let i = row_begin; i <= row_end; i++) {
    const temp = sort_data[i - 1].reduce((a, c) => a + (c % i), 0);
    answer ^= temp;
  }

  return answer;
}