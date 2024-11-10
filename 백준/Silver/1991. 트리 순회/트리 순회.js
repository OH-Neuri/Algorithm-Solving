const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input.shift());
const graph = new Map();

for (let i = 0; i < N; i++) {
  const [node, left, right] = input[i].trim().split(" ");
  graph.set(node, [left, right]);
}

//console.log(graph);
// 전위 순회 루트>왼>오
function preorder(node, answer) {
  if (node == ".") return "";

  answer.push(node);
  preorder(graph.get(node)[0], answer);
  preorder(graph.get(node)[1], answer);
}

// 중위 순회
function inorder(node, answer) {
  if (node == ".") return "";

  inorder(graph.get(node)[0], answer);
  answer.push(node);
  inorder(graph.get(node)[1], answer);
}

// 후위 순회
function postorder(node, answer) {
  if (node == ".") return "";

  postorder(graph.get(node)[0], answer);
  postorder(graph.get(node)[1], answer);
  answer.push(node);
}

let answerPre = [];
let answerIn = [];
let answerPost = [];

preorder("A", answerPre);
inorder("A", answerIn);
postorder("A", answerPost);

console.log(answerPre.join(""));
console.log(answerIn.join(""));
console.log(answerPost.join(""));
