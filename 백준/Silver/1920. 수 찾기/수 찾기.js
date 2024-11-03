const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input.shift());
const Aarr = input.shift().split(" ").map(Number);
const M = parseInt(input.shift());
const Marr = input.shift().split(" ").map(Number);

let visit = Array(100001).fill(false);
for (let a of Aarr) {
  visit[a] = true;
}

for (let m of Marr) {
  if (visit[m]) {
    console.log(1);
  } else {
    console.log(0);
  }
}
