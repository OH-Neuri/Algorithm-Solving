function solution(progresses, speeds) {
  let answer = [];

  while (speeds.length > 0) { // speed 배열길이가 0이 될때까지
    let cnt = 0;
    for (let i = 0; i < speeds.length; i++) { // progress와 speed 짝지어 더하기
      if (progresses[i] < 100) { // 100이 넘어가면 그만 더하기
        progresses[i] += speeds[i];
      }
    }
    while (progresses[0] >= 100) { // 맨앞의 progress배열이 100이 넘으면 shift
      progresses.shift();
      speeds.shift(); // speed도 shift
      cnt++;
    }
    if (cnt > 0) {
      answer.push(cnt);
    }
  }
  return answer;
}