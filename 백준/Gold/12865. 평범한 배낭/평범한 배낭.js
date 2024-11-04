const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input.shift().split(" ").map(Number);
const arr = input.map((line) => line.split(" ").map(Number));

let dp = Array(K + 1).fill(0);

for (let [w, v] of arr) {
  let tmpDP = [...dp];
  for (let i = 0; i <= K - w; i++) {
    tmpDP[i + w] = Math.max(dp[i + w], dp[i] + v);
  }
  dp = tmpDP;
}

console.log(dp[K]);
