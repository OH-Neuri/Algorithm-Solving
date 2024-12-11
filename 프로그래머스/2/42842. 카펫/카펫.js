function solution(brown, yellow) {
  const TOTAL = brown + yellow;

  for (let height = 3; height <= Math.sqrt(TOTAL); height++) {
    const remainder = TOTAL % height;

    if (remainder !== 0) continue;

    const width = TOTAL / height;
    if ((width - 2) * (height - 2) === yellow) {
      return [width, height];
    }
  }
}