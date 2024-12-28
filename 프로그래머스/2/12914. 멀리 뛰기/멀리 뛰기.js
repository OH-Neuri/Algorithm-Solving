function solution(n) {
  if (n === 1 || n === 2) return n;
  const dp = Array(n).fill(0);
  const mod = 1234567;
  dp[0] = 1;
  dp[1] = 2;
  for (let i = 2; i < n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
  }
  return dp[n - 1];
}