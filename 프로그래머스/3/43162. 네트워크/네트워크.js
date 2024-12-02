function solution(n, computers) {
    // 네트워크 수 세기
    let networks = 0;

    // 방문 여부 확인하기
    let visit = Array(n).fill(false);
    
    // 방문한 곳인지 확인 및 네트워크 수 증가시키기
    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            networks ++;
            isVisit(i);
        }
    }
    
    // DFS를 통해 방문한 곳인지 확인하는 함수
    function isVisit(index) {
        visit[index] = true;
        
        const computer = computers[index];
        
        for (let i = 0; i < computer.length; i++) {
            const isConnect = computer[i] === 1 ? true : false;
            
            // 방문하지 않았고 && 연결된 곳인지 확인
            if (!visit[i] && isConnect) {
                isVisit(i);
            }
        }        
    }
    
    return networks;
}