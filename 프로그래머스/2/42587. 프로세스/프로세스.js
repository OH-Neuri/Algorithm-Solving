function solution(priorities, location) {
    let answer = 0;
    let index = [];
    let sortedPriorities = priorities.slice().sort((a, b) => b - a); // 우선순위를 내림차순으로 정렬한 배열
    
    for (let i = 0; i < priorities.length; i++) {
        index.push(i); // 인덱스 배열 초기화
    }
    
    while (index.length > 0) {
        let curr = index.shift(); // 현재 인덱스 추출
        if (priorities[curr] < sortedPriorities[0]) { // 현재 작업의 우선순위가 최고 우선순위보다 낮을 때
            index.push(curr); // 다시 큐의 맨 뒤에 추가
        } else { // 현재 작업의 우선순위가 최고 우선순위와 같거나 높을 때
            answer += 1; // 인쇄
            sortedPriorities.shift(); // 최고 우선순위 업데이트
            if (curr === location) { // 요청한 문서일 경우
                return answer; // 인쇄 순서 반환
            }
        }
    }
}

