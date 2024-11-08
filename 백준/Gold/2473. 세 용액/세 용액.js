const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);

arr.sort((a, b) => a - b);

let result = [];
let minValue = Infinity;

for (let i = 0; i < N - 2; i++) {
  const first = arr[i];
  let start = i + 1;
  let end = N - 1;
  let target = -first;
  while (start < end) {
    let sum = first + arr[start] + arr[end];

    if (minValue > Math.abs(sum)) {
      minValue = Math.abs(sum);
      result = [arr[i], arr[start], arr[end]];
    }
    if (target > arr[start] + arr[end]) {
      // 세 용액의 합이 0에 가까운 경우
      start++;
    } else if (target < arr[start] + arr[end]) {
      end--;
    }
    // 합이 0일 경우,
    else {
      console.log(arr[i], arr[start], arr[end]);
      return;
    }
  }
}

console.log(result[0], result[1], result[2]);
