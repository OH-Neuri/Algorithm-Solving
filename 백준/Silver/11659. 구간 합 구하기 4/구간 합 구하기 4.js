const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

let prefixSum = Array(N + 1).fill(0);
let sum = 0;

for (let i = 1; i < N + 1; i++) {
  sum += arr[i - 1];
  prefixSum[i] = sum;
}

let result = [];
for (let tc = 0; tc < M; tc++) {
  const [i, j] = input[tc + 2].split(" ").map(Number);
  result.push(prefixSum[j] - prefixSum[i - 1]);
}

console.log(result.join("\n"));
