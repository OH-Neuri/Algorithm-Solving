const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n");

const N = Number(input.shift());
let area = input.map((item) => item.split(" ").map(Number));

// 최대 높이 찾기
let MAX = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    MAX = Math.max(MAX, area[i][j]);
  }
}

// 안전한 최대 영역 수
let answer = 1;
for (let rain = 0; rain <= MAX; rain++) {
  answer = Math.max(answer, findSafeArea(rain));
}

function findSafeArea(rain) {
  const map = input.map((item) => item.split(" ").map(Number));
  let safeArea = 0;
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  const dir = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];

  // 비의 양 기준으로 잠기는 지역(0), 안전한 지역(1) 구분
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (map[i][j] <= rain) {
        map[i][j] = 0;
      } else map[i][j] = 1;
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (map[i][j] === 1 && !visited[i][j]) {
        safeArea++;
        dfs(i, j);
      }
    }
  }

  function dfs(i, j) {
    if (isValidRange(i, j) && !visited[i][j] && map[i][j] === 1) {
      visited[i][j] = true;
      for (let d of dir) {
        const [dx, dy] = [i + d[0], j + d[1]];
        dfs(dx, dy);
      }
    }
  }

  function isValidRange(i, j) {
    if (i < 0 || i >= N || j < 0 || j >= N) return false;
    else return true;
  }

  return safeArea;
}

console.log(answer);