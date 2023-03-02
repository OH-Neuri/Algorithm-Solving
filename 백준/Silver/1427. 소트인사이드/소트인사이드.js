const fs = require("fs");
// 입력 데이터를 split("")으로 나눠서 배열로 만들고, number 타입으로 전환
let input = fs.readFileSync("/dev/stdin").toString().trim().split("").map((item) => Number(item));

// input 배열을 내림차순으로 정렬
input.sort((a,b) => b - a);

// join("")으로 배열 원소를 공백없이 한번에 이어붙여서 출력
console.log(input.join(""));