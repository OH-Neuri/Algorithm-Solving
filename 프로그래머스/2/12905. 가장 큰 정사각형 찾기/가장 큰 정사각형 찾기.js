function solution(board) {
  let maxLen = 0;
  let m = board.length;
  let n = board[0].length;

  if (m <= 1 || n <= 1) {
    return 1;
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (board[i][j] === 0) {
        continue;
      } else {
        let minNum = Math.min(
          board[i - 1][j],
          board[i][j - 1],
          board[i - 1][j - 1]
        );

        board[i][j] = minNum + 1;

        if (board[i][j] > maxLen) {
          maxLen = board[i][j];
        }
      }
    }
  }

  return maxLen * maxLen;
}