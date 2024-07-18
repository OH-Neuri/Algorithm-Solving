const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let N = Number(input);

let flag = false;

const checkDuplivate = (str) => {
  const len = str.length;
  const searchRange = parseInt(len / 2, 10);
  for (let i = 1; i <= searchRange; i++) {
    if (str.slice(len - i, len) === str.slice(len - 2 * i, len - i)) return true;
  }
};

const dfs = (L, str) => {
  if (flag) return;
  if (checkDuplivate(str)) return; // 나쁜 수열

  if (L == N) {
    console.log(str);
    flag = true;
    return;
  }

  dfs(L + 1, str + "1");
  dfs(L + 1, str + "2");
  dfs(L + 1, str + "3");
};

dfs(0, "");
