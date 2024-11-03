const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input.shift());

const set = new Set(input.map((line) => line.trim()));
const arr = Array.from(set).sort((a, b) => {
  if (a.length == b.length) return a.localeCompare(b);
  return a.length - b.length;
});

for (let a of arr) {
  console.log(a);
}
