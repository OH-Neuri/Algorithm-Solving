const fs = require('fs');

// 입력 처리
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const heights = input[1].split(' ').map(Number);

// 메인 함수
function main() {
  const result = calculateMinHeightDifference(heights, n);
  console.log(result);
}

// 두 눈사람 쌍의 차이 계산
const INF = 1_000_000_000;
function calculateMinHeightDifference(heights, n) {
  heights.sort((a, b) => a - b);
  let result = INF;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const sum1 = heights[i] + heights[j];
      let start = 0;
      let end = n - 1;

      while (start < end) {
        if (start === i || start === j) {
          start++;
          continue;
        }
        if (end === i || end === j) {
          end--;
          continue;
        }

        const sum2 = heights[start] + heights[end];
        result = Math.min(Math.abs(sum2 - sum1), result);

        if (sum1 > sum2) {
          start++;
        } else if (sum1 < sum2) {
          end--;
        } else {
          return 0; // 차이가 0이면 바로 반환
        }
      }
    }
  }

  return result;
}

// 프로그램 실행
main();
