const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const TC = parseInt(input.shift());
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

for (let tc = 0; tc < TC; tc++) {
  const [w, h] = input.shift().split(" ").map(Number);
  let arr = input.splice(0, h).map((i) => i.trim().split(""));
  escapeSK(w, h, arr);
}

function escapeSK(w, h, arr) {
  let fire = []; // 불좌표
  let sk_XY = []; // 상근좌표

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (arr[i][j] == "*") fire.push([i, j, false]);
      if (arr[i][j] == "@") {
        arr[i][j] = ".";
        sk_XY.push([i, j, 1]);
      }
    }
  }

  let queue = [...fire, ...sk_XY];
  let begin = 0;
  let end = queue.length;

  while (begin < end) {
    const [x, y, sk] = queue[begin++];

    for (let k = 0; k < 4; k++) {
      let nx = x + dx[k];
      let ny = y + dy[k];

      // 상근이 탈출
      if (sk > 0 && (nx < 0 || nx >= h || ny < 0 || ny >= w)) {
        return console.log(sk);
      }
      // 배열 나가면 종료
      if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;

      // 앞에 불, 벽 아닐경우 불 이동
      if (!sk && arr[nx][ny] !== "#") {
        arr[nx][ny] = "#";
        queue.push([nx, ny, false]);
        end++;
      }
      // 불 이동, 앞에 벽 아닐 경우
      if (sk && arr[nx][ny] == ".") {
        arr[nx][ny] = "@";
        queue.push([nx, ny, sk + 1]);
        end++;
      }
    }
  }
  return console.log("IMPOSSIBLE");
}
