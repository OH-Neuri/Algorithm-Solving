const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const TC = parseInt(input.shift());
const commands = ["D", "S", "L", "R"];

for (let tc = 0; tc < TC; tc++) {
  const [A, B] = input.shift().split(" ").map(Number);
  console.log(convertAtoB(A, B));
}

function convertAtoB(A, B) {
  let visited = Array.from({ length: 10050 }, () => false);
  let begin = 0;
  let end = 1;
  let queue = [[A, ""]]; //숫자, 계산기록

  while (begin < end) {
    const [num, operation] = queue[begin++];
    if (num == B) return operation;

    for (const c of commands) {
      const newNums = executeCommand(num, c);

      if (!visited[newNums]) {
        visited[newNums] = true;
        queue.push([newNums, operation + c]);
        end++;
      }
    }
  }
}

function executeCommand(number, command) {
  if (command === "D") {
    return (number * 2) % 10000;
  } else if (command === "S") {
    return (number + 9999) % 10000;
  } else if (command === "L") {
    return (number % 1000) * 10 + Math.floor(number / 1000);
  } else if (command === "R") {
    return (number % 10) * 1000 + Math.floor(number / 10);
  }
}
