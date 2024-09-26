const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input.shift());
const students = input.shift().split(" ").map(Number);

// 학생 배열을 오름차순으로 정렬
const sortedStudents = students.sort((a, b) => a - b);

let result = 0;

// 첫 번째 학생을 고정하고 나머지 두 학생을 투 포인터로 찾는 방식
for (let i = 0; i < N - 2; i++) {
  let left = i + 1;
  let right = N - 1;

  while (left < right) {
    const sum = sortedStudents[i] + sortedStudents[left] + sortedStudents[right];

    if (sum === 0) {
      // 합이 0일 때 처리 - 중복된 값 처리
      if (sortedStudents[left] === sortedStudents[right]) {
        // left와 right 값이 동일한 경우 가능한 조합의 수 계산
        const count = right - left + 1;
        result += (count * (count - 1)) / 2;  // 조합 공식: nC2
        break;
      } else {
        // left와 right 값이 다른 경우 각각 중복된 값의 개수를 세고 곱함
        let leftCount = 1;
        let rightCount = 1;

        // 왼쪽 포인터 값이 중복된 경우 처리
        while (left + 1 < right && sortedStudents[left] === sortedStudents[left + 1]) {
          leftCount++;
          left++;
        }

        // 오른쪽 포인터 값이 중복된 경우 처리
        while (right - 1 > left && sortedStudents[right] === sortedStudents[right - 1]) {
          rightCount++;
          right--;
        }

        // 중복된 값의 곱을 결과에 추가
        result += leftCount * rightCount;

        // 포인터 이동
        left++;
        right--;
      }
    } else if (sum < 0) {
      left++;  // 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
    } else {
      right--;  // 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
    }
  }
}

console.log(result);
