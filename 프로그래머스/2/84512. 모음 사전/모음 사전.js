function solution(word) {
  let answer = 0;
  const vowels = ["A", "E", "I", "O", "U"];
  const counts = [781, 156, 31, 6, 1];

  for (let i = 0; i < word.length; i++) {
    answer += vowels.indexOf(word[i]) * counts[i] + 1;
  }

  return answer;
}