function solution(s) {
  let ans = s.length; // 최악의 압축 효율일 때로 초기화

  // 압축하는 문자열 개수 1개씩 증가
  for (let i = 1; i < s.length; i++) {
    let count = 1; // 압축된 문자열 개수 카운팅
    let temp = s.slice(0, i); // 현재 비교할 문자 저장
    let afterS = ""; // 압축 후 문자열

    // 문자열 순회 (temp로 맨 앞의 문자열 잘랐기 때문에 i부터 시작)
    for (let j = i; j < s.length; j += i) {
      // 저장된 문자가 현재 문자와 같다면
      if (temp === s.slice(j, j + i)) {
        count += 1; // 압축 개수 + 1
      } else {
        // 압축한 문자가 없다면
        if (count === 1) {
          afterS += temp; // 문자 추가
        } else {
          afterS += count + temp; // 압축한 개수와 문자 추가
        }

        count = 1; // 압축 개수 초기화
        temp = s.slice(j, j + i); // 다음 비교 문자로 갱신
      }
    }

    // 문자열 순회가 끝난 후
    if (count === 1) {
      afterS += temp;
    } else {
      afterS += count + temp;
    }

    // 압축 후 문자열 길이와 비교
    ans = Math.min(ans, afterS.length);
  }

  return ans;
}