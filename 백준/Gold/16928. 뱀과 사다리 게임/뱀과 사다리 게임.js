const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const ladder = input.slice(0, N).map((line) => line.split(" ").map(Number));
const snake = input.map((line) => line.split(" ").map(Number));

let matrix = Array(101).fill(Infinity); // 방문 배열
matrix[0] = 0;
matrix[1] = 0; // 출발지
let queue = [[1, 0]]; // 위치, 주사위 횟수
let begin = 0;
let end = 1;

while (begin < end) {
  let [position, diceCnt] = queue[begin++];

  if (position === 100) {
    console.log(diceCnt);
    break;
  }

  for (let i = 6; i > 0; i--) {
    let newPosition = position + i;

    if (newPosition > 100) continue;

    if (matrix[position + i] == Infinity || matrix[position + i] > diceCnt) {
      // 사다리 of 뱀
      let move = movePosition(ladder, newPosition) || movePosition(snake, newPosition);

      if (move) {
        matrix[move] = diceCnt + 1;
        queue.push([move, diceCnt + 1]);
      } else {
        matrix[newPosition] = diceCnt + 1;
        queue.push([newPosition, diceCnt + 1]);
      }
      end++;
    }
  }
}

function movePosition(arr, i) {
  for (let [start, end] of arr) {
    if (start === i) return end;
  }
  return 0;
}
