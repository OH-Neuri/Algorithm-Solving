const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input[0]);
const nums = input[1].split(" ").map(Number);
nums.sort((a, b) => a - b);

let mixSum = Infinity;
let answer = [];
let start = 0;
let end = N - 1;

while (start < end) {
  let sum = nums[start] + nums[end];

  if (sum == 0) return console.log(nums[start], nums[end]);

  if (mixSum > Math.abs(sum)) {
    mixSum = Math.abs(sum);
    answer = [nums[start], nums[end]];
  }

  if (sum > 0) {
    end--;
  } else {
    start++;
  }
}

console.log(answer[0], answer[1]);
