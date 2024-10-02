function solution(arr) {
    var answer = [0, 0]; 

    function compress(x, y, size) {
        if (size === 1) {
            answer[arr[x][y]]++; // 해당 위치의 값에 따라 0 또는 1의 개수 증가
            return;
        }

        let zeroCount = 0;
        let oneCount = 0;
        let halfSize = size / 2;

        // 현재 영역을 4등분하여 재귀적으로 처리
        for (let i = x; i < x + size; i++) {
            for (let j = y; j < y + size; j++) {
                if (arr[i][j] === 0) zeroCount++;
                else oneCount++;
            }
        }

        // 현재 영역이 압축되지 않은 경우
        if (zeroCount !== 0 && oneCount !== 0) {
            // 4등분하여 재귀 호출
            compress(x, y, halfSize);
            compress(x, y + halfSize, halfSize);
            compress(x + halfSize, y, halfSize);
            compress(x + halfSize, y + halfSize, halfSize);
        } else {
            // 압축된 경우
            if (zeroCount !== 0) answer[0]++; // 0의 개수 증가
            else answer[1]++; // 1의 개수 증가
        }
    }

    compress(0, 0, arr.length);

    return answer;
}