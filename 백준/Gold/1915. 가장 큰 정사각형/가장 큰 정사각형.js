const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const arr = input.map((line) => line.trim().split("").map(Number));
let dp = Array.from({ length: N }, () => Array(M).fill(0));

if (N == 1 && M == 1 && arr[0][0] == 1) {
  console.log(1);
  return;
}

let result = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (arr[i][j] == 1) {
      //모서리
      if (i - 1 < 0 || j - 1 < 0) {
        dp[i][j] = 1;
        result = Math.max(result, dp[i][j]);

        continue;
      }
      // arr 3개가 1일때
      if (arr[i - 1][j - 1] == 1 && arr[i - 1][j] == 1 && arr[i][j - 1] == 1) {
        // dp 3개가 같고 0이 아닐때
        if (
          dp[i - 1][j - 1] == dp[i][j - 1] &&
          dp[i][j - 1] == dp[i - 1][j] &&
          dp[i - 1][j - 1] !== 0
        ) {
          // 1을 더해
          dp[i][j] = dp[i][j - 1] + 1;
        } else {
          // 최소에서 1더해
          dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1;
        }
      } else {
        //
        dp[i][j] = 1;
      }
    } else {
      dp[i][j] = 0;
    }
    result = Math.max(result, dp[i][j]);
  }
}

console.log(result ** 2);
