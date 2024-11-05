const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const [N, M] = input.shift().split(" ").map(Number);
const arr = input.map((line) => line.trim().split("").map(Number));
let visit = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => Array(2).fill(false))
); // 안부수고 온 경우, 부수고온경우
let result = Infinity;

function bfs() {
  visit[0][0][0] = true;
  let queue = [[0, 0, false, 1]]; //위치, 제거유무, 거리
  let begin = 0;
  let end = 1;

  while (begin < end) {
    const [x, y, remove, dist] = queue[begin++];

    if (x == N - 1 && y == M - 1) {
      return (result = Math.min(result, dist));
    }

    for (let k = 0; k < 4; k++) {
      const nx = x + dir[k][0];
      const ny = y + dir[k][1];

      if (nx >= N || nx < 0 || ny >= M || ny < 0) continue;

      // 장애물을 부수고 왔는데, 이미 지나간 자리가 아니면
      if (remove && arr[nx][ny] !== 1 && !visit[nx][ny][1]) {
        visit[nx][ny][1] = true;
        queue.push([nx, ny, remove, dist + 1]);
        end++;
      } else if (!remove && !visit[nx][ny][0]) {
        // 장애물을 만났을 경우
        if (arr[nx][ny] == 1) {
          visit[nx][ny][1] = true;
          queue.push([nx, ny, true, dist + 1]);
        }
        // 장애물을 만나지 않은 경우
        else {
          visit[nx][ny][0] = true;
          queue.push([nx, ny, false, dist + 1]);
        }
        end++;
      }
    }
  }
}

bfs();

if (result == Infinity) {
  console.log(-1);
} else {
  console.log(result);
}
