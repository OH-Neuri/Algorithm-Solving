function reverse(str) {
  return str.slice(1, str.length - 1).split("").map((c) => (c === "(" ? ")" : "(")).join("");
}

function solution(p) {
  if (p.length < 1) return "";

  let balance = 0;
  let pivot = 0;
  do { balance += p[pivot++] === "(" ? 1 : -1 } while (balance !== 0);

  const u = p.slice(0, pivot);
  const v = solution(p.slice(pivot, p.length));

  if (u[0] === "(" && u[u.length - 1] == ")") return u + v;
  else return "(" + v + ")" + reverse(u);
}