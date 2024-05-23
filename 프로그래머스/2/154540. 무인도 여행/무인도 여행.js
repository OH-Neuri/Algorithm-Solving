function solution(maps) {
  const result = [];
  const [R, C] = [maps.length, maps[0].length];
  const visited = Array.from({ length: R }, () => Array(C).fill(0));
  const move = [[0, 1], [0, -1], [1, 0], [-1, 0]];

  const bfs = (a, b) => {
    let cnt = 0;
    const q = [[a, b]];
    cnt += parseInt(maps[a][b]);
    visited[a][b] = 1;

    while (q.length) {
      const [r, c] = q.shift();
      for (let i = 0; i < 4; i++) {
        const nr = r + move[i][0];
        const nc = c + move[i][1];
        if (nr >= 0 && nc >= 0 && nr < R && nc < C && 
            !visited[nr][nc] && maps[nr][nc] !== "X") {
          visited[nr][nc] = 1;
          cnt += parseInt(maps[nr][nc]);
          q.push([nr, nc]);
        }
      }
    }
    result.push(cnt);
  };

  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      if (!visited[i][j] && maps[i][j] !== "X") bfs(i, j);
    }
  }

  if (result.length === 0) return [-1];

  return result.sort((a, b) => a - b);
}