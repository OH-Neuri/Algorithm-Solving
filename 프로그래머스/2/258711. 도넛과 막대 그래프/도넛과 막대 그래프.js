function solution(edges) {
    const N = 1_000_001;
    const inDeg = Array(N).fill(0);
    const outDeg = Array(N).fill(0);
    const graph = Array.from({ length: N }, () => []);

    for (const [from, to] of edges) {
        graph[from].push(to);
        outDeg[from]++;
        inDeg[to]++;
    }

    let start = 0;
    for (let i = 0; i < N; i++) {
        if (inDeg[i] === 0 && outDeg[i] >= 2) {
            start = i;
            break;
        }
    }

    let donut = 0, stick = 0, eight = 0;

    for (const next of graph[start]) {
        let node = next;
        const visited = new Set();

        while (true) {
            if (visited.has(node)) {
                // 사이클이면서, 분기 없는 도넛
                donut++;
                break;
            }
            visited.add(node);

            if (outDeg[node] === 0) {
                // 막대
                stick++;
                break;
            }

            if (outDeg[node] >= 2) {
                // 중간에 분기점 있음 → 8자
                eight++;
                break;
            }

            node = graph[node][0]; // 다음 노드 
        }
    }

    return [start, donut, stick, eight];
}
