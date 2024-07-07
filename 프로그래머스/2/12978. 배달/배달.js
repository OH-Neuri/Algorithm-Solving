function solution(N, road, K) {
  const arr = Array(N + 1).fill(Number.MAX_SAFE_INTEGER); // K보다 커야함으로 Infinity 값 설정
  const lines = Array.from(Array(N + 1), () => []); // N+1만큼의 방 생성

  for (let value of road) {
    // 연결된 경로를 모두 lines에 저장
    let [a, b, c] = value;
    lines[a].push({ to: b, cost: c });
    lines[b].push({ to: a, cost: c });
  }

  let queue = [{ to: 1, cost: 0 }];
  arr[1] = 0;

  while (queue.length) {
    // queue가 빈 배열이 될 때까지 반복
    let { to } = queue.pop();
    for (let line of lines[to]) {
      if (arr[line.to] > arr[to] + line.cost) {
        // 기존값보다 우회값이 더 작으면 우회값으로 저장
        arr[line.to] = arr[to] + line.cost;
        queue.push(line);
      }
    }
  }

  return arr.filter((v) => v <= K).length; // K보다 작은 경로의 수를 반환
}