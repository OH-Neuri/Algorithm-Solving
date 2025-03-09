const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [m, n] = input[0].split(" ").map(Number);
const arr = input.slice(1).map((line) => line.split(" ").map(Number));
const dp = Array.from({ length: m }, () => Array(n).fill(-1));

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

function DFS(y, x) {
  if (y === m - 1 && x === n - 1) return 1;
  if (dp[y][x] !== -1) return dp[y][x];

  dp[y][x] = 0;

  for (let k = 0; k < 4; k++) {
    const ny = y + dir[k][0];
    const nx = x + dir[k][1];
    if (ny < 0 || ny >= m || nx < 0 || nx >= n) continue;
    if (arr[y][x] > arr[ny][nx]) {
      dp[y][x] += DFS(ny, nx);
    }
  }
  return dp[y][x];
}

DFS(0, 0);

console.log(dp[0][0]);
