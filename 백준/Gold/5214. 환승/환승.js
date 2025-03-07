const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k, m] = input[0].split(" ").map(Number);
const node = Array.from({ length: n + m + 1 }, () => []);
const visited = Array(n + m + 1).fill(false);

if (n === 1) {
  console.log(1);
  return;
}

// 하이퍼튜브를 그래프에 추가
for (let i = 1; i <= m; i++) {
  let h = i + n;
  let hNode = input[i].split(" ").map(Number);
  for (let station of hNode) {
    node[h].push(station);
    node[station].push(h);
  }
}

function bfs(start) {
  const queue = [[start, 1]]; // 역 번호, 이동 횟수
  visited[start] = true;
  let index = 0;

  while (index < queue.length) {
    const [curr, cnt] = queue[index++];

    if (curr === n) return cnt; // 목적지 도달

    for (let next of node[curr]) {
      if (!visited[next]) {
        visited[next] = true;
        const nextCnt = curr > n ? cnt : cnt + 1;

        queue.push([next, nextCnt]);
      }
    }
  }

  return -1;
}

console.log(bfs(1));
