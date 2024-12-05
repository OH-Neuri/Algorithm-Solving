function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);
  return A.reduce((sum, curr, i) => sum + curr * B[i], 0);
}