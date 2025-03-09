const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const students = input.map((line) => line.trim().split(""));
const linearStudents = [];
const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

// 5x5 격자의 좌표를 1차원으로 변환
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    linearStudents.push(i * 5 + j);
  }
}

let result = 0;

// 7명의 조합을 구한 후, 연결 여부를 판별
for (let combination of getCombination(linearStudents, 7)) {
  const combinationCoords = getCombinationCoords(combination);

  // "S"가 4개 이상인지 체크
  let sCount = combinationCoords.reduce(
    (count, [y, x]) => count + (students[y][x] === "S" ? 1 : 0),
    0
  );
  if (sCount < 4) continue;

  const visited = new Set();
  visited.add(`${combinationCoords[0][0]}-${combinationCoords[0][1]}`);

  //  DFS를 실행하고, 방문한 개수를 반환하여 7개인지 확인
  if (
    isConnected(
      combinationCoords[0][0],
      combinationCoords[0][1],
      visited,
      combinationCoords
    ) === 7
  ) {
    result++;
  }
}

console.log(result);

//  DFS 함수 (방문 개수를 반환하여 7개인지 확인)
function isConnected(y, x, visited, combinationCoords) {
  let count = 1; // 현재 방문한 좌표 개수

  for (let k = 0; k < 4; k++) {
    let ny = y + dir[k][0];
    let nx = x + dir[k][1];

    if (
      combinationCoords.some(([cy, cx]) => cy === ny && cx === nx) &&
      !visited.has(`${ny}-${nx}`)
    ) {
      visited.add(`${ny}-${nx}`);
      count += isConnected(ny, nx, visited, combinationCoords); //  방문 개수 누적
    }
  }

  return count;
}

// 조합된 인덱스를 좌표값으로 변환하는 함수
function getCombinationCoords(arr) {
  return arr.map((index) => [Math.floor(index / 5), index % 5]);
}

// 조합 생성 함수
function getCombination(arr, selectNumber) {
  if (selectNumber === 0) return [[]];
  if (arr.length === 0) return [];

  const first = arr[0];
  const rest = arr.slice(1);

  const withFirst = getCombination(rest, selectNumber - 1).map((comb) => [
    first,
    ...comb,
  ]);
  const withoutFirst = getCombination(rest, selectNumber);

  return withFirst.concat(withoutFirst);
}
