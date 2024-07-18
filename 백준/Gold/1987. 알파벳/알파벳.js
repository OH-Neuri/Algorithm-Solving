const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [R, C] = input.shift().split(" ").map(Number);

let arr = input.map((line) => line.trim().split(""));
let visited = Array.from({ length: R }, () => Array.from({ length: C }, () => false));
let result = 0;
let dx = [0, 1, 0, -1];
let dy = [1, 0, -1, 0];
let alp = Array.from({ length: 26 }, () => false);

const DFS = (x, y, dist) => {
  result = Math.max(result, dist);
  alp[arr[x][y].charCodeAt() - 65] = true;
  visited[x][y] = true;

  for (let k = 0; k < 4; k++) {
    let nx = x + dx[k];
    let ny = y + dy[k];
    if (
      0 <= nx &&
      nx < R &&
      0 <= ny &&
      ny < C &&
      !visited[nx][ny] &&
      !alp[arr[nx][ny].charCodeAt() - 65]
    ) {
      DFS(nx, ny, dist + 1);
    }
  }
  visited[x][y] = false;
  alp[arr[x][y].charCodeAt() - 65] = false;
};

DFS(0, 0, 1);
console.log(result);
