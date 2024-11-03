const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const N = parseInt(input);

let cnt = 0;
let val = 666;
while (cnt < N) {
  let check = val.toString();
  if (check.includes("666")) {
    cnt++;
  }
  val++;
}

console.log(val - 1);
