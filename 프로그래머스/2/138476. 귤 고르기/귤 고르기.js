function solution(k, tangerine) {
  let answer = 0;
  const tDict = {};

  // 중복 값 개수 count
  tangerine.forEach((t) => (tDict[t] = (tDict[t] || 0) + 1));

  // value(중복 값 개수)를 내림차순으로 정렬
  const tArr = Object.values(tDict).sort((a, b) => b - a);

  // 필요한 귤만큼 가짓수를 더해줍니다
  for (const t of tArr) {
    answer++;
    if (k > t) k -= t;
    else break;
  }

  return answer;
}