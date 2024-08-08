function solution(n, roads, sources, destination) {
    // 노드 저장
    let graph = Array.from({length: n + 1}, () => []);
    let costs = Array.from({length: n + 1}, () => -1); // 초기값을 -1로 설정

    // 그래프 초기화
    for (let [s, e] of roads) {
        graph[s].push(e);
        graph[e].push(s);
    }

    // BFS 시작
    let queue = [destination];
    costs[destination] = 0; // 목적지의 거리는 0

    let begin = 0;
    while (begin < queue.length) {
        let curr = queue[begin++];
        let currDist = costs[curr];

        for (let next of graph[curr]) {
            if (costs[next] === -1) { // 아직 방문하지 않은 노드
                costs[next] = currDist + 1;
                queue.push(next);
            }
        }
    }

    // 출발 노드에 대한 결과를 반환
    return sources.map(source => costs[source]);
}
