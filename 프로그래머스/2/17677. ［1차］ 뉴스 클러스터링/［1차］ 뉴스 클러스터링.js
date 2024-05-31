function solution(str1, str2) {
  // 대소문자 구별 안 한다고 했으므로 모두 소문자로 만들기
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  let str1_arr = [];
  let intersection = 0; // 교집합의 크기
  let union = 0; // 합집합의 크기

  // str1을 두 글자씩 끊었을 때 소문자로만 이루어졌다면 str1_arr에 넣기
  for (let i = 0; i < str1.length - 1; i++) {
    if (
      str1.charCodeAt(i) >= 97 &&
      str1.charCodeAt(i) <= 122 &&
      str1.charCodeAt(i + 1) >= 97 &&
      str1.charCodeAt(i + 1) <= 122
    )
      str1_arr.push(str1.slice(i, i + 2));
  }

  // str2를 모르는 상황에서 합집합의 길이는 str1_arr의 길이와 같음
  union += str1_arr.length;

  // str2을 두 글자씩 끊었을 때 소문자로만 이루어졌다면
  for (let i = 0; i < str2.length - 1; i++) {
    if (
      str2.charCodeAt(i) >= 97 &&
      str2.charCodeAt(i) <= 122 &&
      str2.charCodeAt(i + 1) >= 97 &&
      str2.charCodeAt(i + 1) <= 122
    ) {
      // 소문자로만 이루어진 두 글자
      const word = str2.slice(i, i + 2);

      // str1_arr과 교집합 발견한 경우
      if (str1_arr.includes(word)) {
        intersection++;
        // 다중집합 고려하기
        str1_arr.splice(str1_arr.indexOf(word), 1);
      } else union++; // 교집합 될 수 없는 경우
    }
  }

  // 두 집합이 모두 공집합인 경우 구분
  return union === 0 ? 65536 : Math.floor((intersection / union) * 65536);
}