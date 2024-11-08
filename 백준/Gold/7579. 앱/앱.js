const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const memory = input[1].split(" ").map(Number);
const cost = input[2].split(" ").map(Number);

const sumCost = cost.reduce((acc, cur) => acc + cur, 0);
const dp = Array.from({ length: N + 1 }, () => Array(sumCost + 1).fill(0));

let result = Infinity;

for (let i = 1; i <= N; i++) {
  const currentMemory = memory[i - 1];
  const currentCost = cost[i - 1];

  for (let j = 0; j <= sumCost; j++) {
    if (j >= currentCost) {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - currentCost] + currentMemory);
    } else {
      dp[i][j] = dp[i - 1][j];
    }

    if (dp[i][j] >= M) {
      result = Math.min(result, j);
    }
  }
}

console.log(result);
