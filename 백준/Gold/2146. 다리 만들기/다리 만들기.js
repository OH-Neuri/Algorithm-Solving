const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const dir = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];
const N = Number(input.shift());
let arr = input.map((line) => line.trim().split(" ").map(Number));

function connect(start, currentLandVisited) {
  let bridgeVisited = Array.from({ length: N }, () => Array(N).fill(false));

  while (start.length > 0) {
    const [x, y, bridge] = start.shift();

    for (let [dx, dy] of dir) {
      const nx = x + dx;
      const ny = y + dy;
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
      // 자기 땅이 아니고 다리가 연결되지 않았을 경우,
      if (!currentLandVisited[nx][ny] && !bridgeVisited[nx][ny]) {
        //  바다
        if (arr[nx][ny] == 0) {
          bridgeVisited[nx][ny] = true;
          start.push([nx, ny, bridge + 1]);
        } else {
          // 다른 육지
          minBridge = Math.min(minBridge, bridge);
          return 
        }
      }
    }
  }
}

function bfs(i, j, landVisited) {
  let currentLandVisited = Array.from({ length: N }, () => Array(N).fill(false));
  let queue = [[i, j]];
  let begin = 0;
  let end = 1;
  landVisited[i][j] = true;
  currentLandVisited[i][j] = true;
  let start = [[i, j, 0]]; // 출발할 육지 좌표 모음

  while (begin < end) {
    let [x, y] = queue[begin++];

    for (let [dx, dy] of dir) {
      const nx = x + dx;
      const ny = y + dy;
      if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
      if (!landVisited[nx][ny] && arr[nx][ny] == 1) {
        landVisited[nx][ny] = true;
        currentLandVisited[nx][ny] = true;
        queue.push([nx, ny]);
        start.push([nx, ny, 0]);
        end++;
      }
    }
  }
  connect(start, currentLandVisited);
}

let minBridge = Infinity;
let landVisited = Array.from({ length: N }, () => Array(N).fill(false));
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (arr[i][j] == 1 && !landVisited[i][j]) {
      bfs(i, j, landVisited);
    }
  }
}

console.log(minBridge);
