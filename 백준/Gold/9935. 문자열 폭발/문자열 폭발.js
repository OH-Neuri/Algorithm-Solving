const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const S = input.shift().trim(); // ""
const target = input.shift().trim(); // ""
const len = target.length;
let stack = [];

for (let i = 0; i < S.length; i++) {
  stack.push(S[i]);

  // 마지막 문자가 같으면,
  if (S[i] == target[len - 1]) {
    const last = stack.slice(-len);
    if (last.join("") === target) {
      stack.splice(-len);
    }
  }
}
// 여기서 str이 빈 문자열이면 "FRULA"를 출력하도록 수정
if (stack.length) {
  console.log(stack.join(""));
} else {
  console.log("FRULA");
}
