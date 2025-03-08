const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const k = Number(input[0]);
const [w, h] = input[1].split(" ").map(Number);
let arr = input.splice(2).map((line) => line.split(" ").map(Number));

// visited[y][x][k] : (x, y)에서 k번 말 이동을 사용한 경우의 방문 여부
let visited = Array.from({ length: h }, () =>
  Array.from({ length: w }, () => Array(k + 1).fill(false))
);

const kMove = [
  [-2, -1], [-2, 1], [-1, -2], [-1, 2],
  [1, -2], [1, 2], [2, -1], [2, 1]
];

const nMove = [
  [0, -1], [0, 1], [1, 0], [-1, 0]
];

function bfs() {
  const queue = [];
  queue.push([0, 0, 0, 0]); // (x, y, 말 이동 횟수, 이동 횟수)
  visited[0][0][0] = true;
  let begin = 0;

  while (begin < queue.length) {
    const [cx, cy, kCheck, cnt] = queue[begin++];
    
    // 도착 지점에 도달하면 최소 이동 횟수 반환
    if (cx === w - 1 && cy === h - 1) return cnt;

    // 말 이동 (k번 이하로 사용 가능)
    if (kCheck < k) {
      for (let [mx, my] of kMove) {
        const nx = cx + mx;
        const ny = cy + my;
        if (nx >= 0 && nx < w && ny >= 0 && ny < h && arr[ny][nx] === 0 && !visited[ny][nx][kCheck + 1]) {
          visited[ny][nx][kCheck + 1] = true;
          queue.push([nx, ny, kCheck + 1, cnt + 1]);
        }
      }
    }

    // 원숭이 이동
    for (let [mx, my] of nMove) {
      const nx = cx + mx;
      const ny = cy + my;
      if (nx >= 0 && nx < w && ny >= 0 && ny < h && arr[ny][nx] === 0 && !visited[ny][nx][kCheck]) {
        visited[ny][nx][kCheck] = true;
        queue.push([nx, ny, kCheck, cnt + 1]);
      }
    }
  }

  return -1;
}

console.log(bfs());
