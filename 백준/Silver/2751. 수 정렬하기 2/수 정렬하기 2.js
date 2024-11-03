const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input.shift());
const num = input.map(Number).sort((a, b) => a - b);

console.log(num.join("\n"));
