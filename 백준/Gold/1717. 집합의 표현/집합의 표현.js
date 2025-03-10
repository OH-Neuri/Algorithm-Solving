const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const parent = Array(n + 1)
  .fill(0)
  .map((_, i) => i);
const rank = Array(n + 1).fill(1);

// find 함수
function find(x) {
  if (parent[x] !== x) {
    parent[x] = find(parent[x]);
  }

  return parent[x];
}

function union(x, y) {
  const rootX = find(x);
  const rootY = find(y);

  if (rank[rootX] > rank[rootY]) {
    parent[rootY] = rootX;
  } else {
    parent[rootX] = rootY;
    if (rank[rootX] === rank[rootY]) {
      rank[rootY]++;
    }
  }
}

const result = [];

for (let i = 1; i <= m; i++) {
  const [command, a, b] = input[i].split(" ").map(Number);

  if (command === 0) {
    union(a, b);
  } else {
    if (find(a) === find(b)) {
      result.push("YES");
    } else {
      result.push("NO");
    }
  }
}

console.log(result.join("\n"));
