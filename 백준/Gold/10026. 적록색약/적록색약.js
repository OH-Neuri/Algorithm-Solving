const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input.shift());
const arr = input.map((line) => line.trim().split(""));
let oneColorVisit = Array.from({ length: N }, () =>
  Array.from({ length: N }, () => false)
);
let RGColorVisit = Array.from({ length: N }, () =>
  Array.from({ length: N }, () => false)
);

let colorCnt = { R: 0, G: 0, B: 0, RG: 0 };

const dir = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

// R, G, B
function BFSOneColor(i, j) {
  oneColorVisit[i][j] = true;
  colorCnt[arr[i][j]]++;
  let queue = [[i, j, arr[i][j]]];
  let begin = 0;
  let end = 1;
  while (begin < end) {
    const [x, y, color] = queue[begin++];
    for (let k = 0; k < 4; k++) {
      const nx = x + dir[k][0];
      const ny = y + dir[k][1];

      if (nx >= N || nx < 0 || ny >= N || ny < 0) continue;
      // 하나의 컬러일 때
      if (!oneColorVisit[nx][ny] && arr[nx][ny] == color) {
        oneColorVisit[nx][ny] = true;
        queue.push([nx, ny, color]);
        end++;
      }
    }
  }
}

// R, G
function BFSRGColor(i, j) {
  RGColorVisit[i][j] = true;
  colorCnt["RG"]++;
  let queue = [[i, j]];
  let begin = 0;
  let end = 1;
  while (begin < end) {
    const [x, y] = queue[begin++];

    for (let k = 0; k < 4; k++) {
      const nx = x + dir[k][0];
      const ny = y + dir[k][1];

      if (nx >= N || nx < 0 || ny >= N || ny < 0) continue;
      if (!RGColorVisit[nx][ny] && (arr[nx][ny] == "R" || arr[nx][ny] == "G")) {
        RGColorVisit[nx][ny] = true;
        queue.push([nx, ny]);
        end++;
      }
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (!oneColorVisit[i][j]) BFSOneColor(i, j);
    if (!RGColorVisit[i][j] && (arr[i][j] == "R" || arr[i][j] == "G")) BFSRGColor(i, j);
  }
}
console.log(
  colorCnt["R"] + colorCnt["G"] + colorCnt["B"],
  colorCnt["RG"] + colorCnt["B"]
);
