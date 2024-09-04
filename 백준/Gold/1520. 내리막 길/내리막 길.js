const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [M, N] = input.shift().trim().split(" ").map(Number);
const arr = input.map((i) => i.trim().split(" ").map(Number));
const dp = Array.from({ length: M }, () => Array.from({ length: N }, () => -1));

function recur(i, j) {
  if (i == M - 1 && j == N - 1) return 1;
  if (dp[i][j] !== -1) return dp[i][j];

  dp[i][j] = 0;

  for (let [x, y] of [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ]) {
    const nx = i + x;
    const ny = j + y;

    if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
      if (arr[i][j] > arr[nx][ny]) {
        dp[i][j] += recur(nx, ny);
      }
    }
  }
  return dp[i][j];
}

console.log(recur(0, 0));
