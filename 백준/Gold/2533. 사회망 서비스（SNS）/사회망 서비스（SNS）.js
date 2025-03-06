const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);

const node = Array.from({ length: n + 1 }, () => []);
const visited = Array(n + 1).fill(false);
const dp = Array.from({ length: n + 1 }, () => [0, 0]);

for (let i = 1; i < n; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  node[a].push(b);
  node[b].push(a);
}

dfs(1);

console.log(Math.min(dp[1][0], dp[1][1]));

function dfs(cur) {
  visited[cur] = true;
  dp[cur][1] = 1;

  for (let next of node[cur]) {
    if (visited[next]) continue;
    dfs(next);
    dp[cur][0] += dp[next][1];
    dp[cur][1] += Math.min(dp[next][0], dp[next][1]);
  }
}
