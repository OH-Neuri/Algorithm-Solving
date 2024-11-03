const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const matrix = input.map((line) => line.trim().split(""));

let result = Infinity;

const sampleW = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
];

const sampleB = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
];

for (let i = 0; i < N - 7; i++) {
  for (let j = 0; j < M - 7; j++) {
    let changeCntW = 64;
    let changeCntB = 64;

    for (let l = 0; l < 8; l++) {
      for (let m = 0; m < 8; m++) {
        if (sampleW[l][m] == matrix[i + l][j + m]) changeCntW--;
        if (sampleB[l][m] == matrix[i + l][j + m]) changeCntB--;
      }
    }

    let minChange = Math.min(changeCntW, changeCntB);
    result = Math.min(result, minChange);
  }
}

console.log(result);
