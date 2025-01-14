function solution(n, stations, w) {
    let answer = 0;
    let range = 2 * w + 1; // 기지국 하나가 커버하는 범위
    let current = 1; // 현재 처리 중인 아파트 번호

    for (let station of stations) {
        let leftEnd = station - w; // 현재 기지국의 왼쪽 끝

        // 전파되지 않은 구간 길이를 계산
        if (current < leftEnd) {
            let uncoveredLength = leftEnd - current; // 전파되지 않은 구간
            answer += Math.ceil(uncoveredLength / range); // 필요한 기지국 개수 추가
        }

        // 현재 위치를 기지국의 오른쪽 범위 이후로 갱신
        current = station + w + 1;
    }

    // 마지막 기지국 이후의 구간 처리
    if (current <= n) {
        let remainingLength = n - current + 1;
        answer += Math.ceil(remainingLength / range);
    }

    return answer;
}
