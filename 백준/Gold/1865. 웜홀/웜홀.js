const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

//테스트 케이스
const TC = input.shift();
for (let tc = 0; tc < TC; tc++) {
  //정점, 도로, 웜홀 의 개수
  const [N, M, W] = input.shift().split(" ").map(Number);
  const road = input.splice(0, M);
  const wormhole = input.splice(0, W);

  const links = [];
  for (let [str, end, time] of road.map((v) => v.split(" ").map(Number))) {
    links.push({ str, end, time });
    links.push({ str: end, end: str, time });
  }
  for (let [str, end, time] of wormhole.map((v) => v.split(" ").map(Number))) {
    links.push({ str, end, time: -time });
  }

  const nodes = Array(N + 1).fill(0);
  for (let i = 1; i <= N; i++) {
    for (let { str, end, time } of links) {
      if (nodes[str] + time < nodes[end]) {
        nodes[end] = nodes[str] + time;
      }
    }
  }
  let pass = "NO";
  A: for (let i = 1; i <= N; i++) {
    for (let { str, end, time } of links) {
      if (nodes[str] + time < nodes[end]) {
        pass = "YES";
        break A;
      }
    }
  }
    console.log(pass);
}
