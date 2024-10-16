const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m, r] = input.shift().split(" ").map(Number);
const items = input.shift().split(" ").map(Number); // 5 7 8 2 3
const dist = Array.from({ length: n + 1 }, () => Array(n + 1).fill(Infinity));

for (let i = 0; i < r; i++) {
  const [s, e, d] = input.shift().split(" ").map(Number);
  dist[s][e] = d;
  dist[e][s] = d;
}
for (let i = 1; i <= n; i++) {
  dist[i][i] = 0;
}

for (let k = 1; k <= n; k++) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      // i에서 k를 거쳐 j로 가는 경로가 더 짧다면 갱신
      if (dist[i][j] > dist[i][k] + dist[k][j]) {
        dist[i][j] = dist[i][k] + dist[k][j];
      }
    }
  }
}

let result = 0;
for (let i = 1; i <= n; i++) {
  let total = 0;
  for (let j = 1; j <= n; j++) {
    if (dist[i][j] <= m) total += items[j - 1];
  }
  result = Math.max(result, total);
}

console.log(result);
