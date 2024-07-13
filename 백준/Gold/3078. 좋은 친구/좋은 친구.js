const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const solution = () => {
  const [N, K] = input.shift().split(" ").map(Number);
  const queue = Array.from(Array(21), () => []);
  let answer = 0;

  input.forEach((name, rank) => {
    const len = name.length;
    // 큐[이름의길이]에서 현재 등수와 K 넘게 차이나는 사람을 제거한다.
    while (queue[len].length > 0 && rank - queue[len][0] > K)
      queue[len].shift();
    answer += queue[len].length;
    queue[len].push(rank);
  });

  console.log(answer);
};

solution(input);