const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const [N, M] = input.shift().trim().split(" ").map(Number);
let arr = input.map((i) => i.trim().split(" ").map(Number));

let time = 0;

function bfs(i, j, visited) {
  let queue = [[i, j]];
  visited[i][j] = true;
  
  while (queue.length > 0) {
    const [x, y] = queue.shift();
    
    for (let [dx, dy] of dir) {
      const nx = x + dx;
      const ny = y + dy;

      if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
      if (!visited[nx][ny] && arr[nx][ny] > 0) {
        visited[nx][ny] = true;
        queue.push([nx, ny]);
      }
    }
  }
}

function melt() {
  let next = arr.map((row) => [...row]);
  
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] > 0) {
        let seaCount = 0;
        for (let [dx, dy] of dir) {
          const nx = i + dx;
          const ny = j + dy;

          if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
          if (arr[nx][ny] === 0) seaCount++;
        }
        next[i][j] = Math.max(0, arr[i][j] - seaCount);
      }
    }
  }
  arr = next;
}

while (true) {
  let icebergCount = 0;
  let visited = Array.from({ length: N }, () => Array(M).fill(false));
  
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] > 0 && !visited[i][j]) {
        icebergCount++;
        bfs(i, j, visited);
      }
    }
  }

  if (icebergCount === 0) {
    console.log(0);
    break;
  }
  
  if (icebergCount >= 2) {
    console.log(time);
    break;
  }

  melt();
  time++;
}
