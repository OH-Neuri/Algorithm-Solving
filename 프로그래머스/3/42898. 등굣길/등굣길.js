function solution(m, n, puddles) {
    const MOD = 1000000007;

    // dp 배열 초기화
    let dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));

    // 물에 잠긴 지역 처리
    let puddleSet = new Set(puddles.map(([x, y]) => `${y},${x}`));
    console.log(puddleSet)
    // 시작 지점 설정
    dp[1][1] = 1;

    // 동적 계획법을 사용하여 경로 계산
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (i === 1 && j === 1) continue; // 시작점은 이미 처리됨
            if (puddleSet.has(`${i},${j}`)) {
                dp[i][j] = 0; // 물에 잠긴 지역
            } else {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;
            }
        }
    }

    return dp[n][m];
}
