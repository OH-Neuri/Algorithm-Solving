const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input.shift().trim().split(" ").map(Number);
const arr = input.map((i) => i.trim().split(" ").map(Number));
const dp = Array.from({ length: N }, () => Array(K + 1).fill(-1));

function knapsackRecursive(i, remainingWeight) {
  // 기저 조건: 모든 물건을 다 고려했거나 배낭에 남은 무게가 0이면 더 이상 넣을 수 없으므로 0 반환
  if (i >= N || remainingWeight === 0) {
    return 0;
  }

  // 이미 계산한 값이 있으면 그 값을 반환
  if (dp[i][remainingWeight] !== -1) {
    return dp[i][remainingWeight];
  }

  const [weight, value] = arr[i]; // i번째 물건의 무게와 가치

  // 1. 현재 물건을 넣지 않는 경우
  let withoutCurrentItem = knapsackRecursive(i + 1, remainingWeight);

  // 2. 현재 물건을 넣는 경우 (단, 남은 무게가 물건의 무게보다 클 때만 가능)
  let withCurrentItem = 0;
  if (remainingWeight >= weight) {
    withCurrentItem = value + knapsackRecursive(i + 1, remainingWeight - weight);
  }

  // 두 경우 중 더 큰 값을 dp 테이블에 저장
  dp[i][remainingWeight] = Math.max(withoutCurrentItem, withCurrentItem);

  return dp[i][remainingWeight];
}
console.log(knapsackRecursive(0, K));

