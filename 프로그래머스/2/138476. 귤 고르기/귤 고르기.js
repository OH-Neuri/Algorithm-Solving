function solution(k, tangerine) {
  var count = 0;

  const sizeObject = tangerine.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});

  let sizeArr = Object.values(sizeObject).sort((a, b) => b - a);

  for (i = 0; i < sizeArr.length; i++) {
    k = k - sizeArr[i];
    count++;
    if (k <= 0) break;
  }

  return count;
}