function solution(board, skill) {
    var answer = 0;
    const c = board.length
    const r = board[0].length
    const degrees = Array.from({length: c+1 }, ()=> Array(r+1).fill(0))
    
    // 스킬 쌓기
    for(const [type, r1, c1, r2, c2, degree] of skill){
        let convertDegress = degree
        if(type === 1) convertDegress *= -1
        
        degrees[r1][c1] += convertDegress
        degrees[r1][c2+1] -= convertDegress
        degrees[r2+1][c1] -= convertDegress
        degrees[r2+1][c2+1] += convertDegress
    }
    
    // 스킬 누적합
    for(let i = 0; i <= c; i++){
        for(let j = 1; j <= r; j++){
            let prev = degrees[i][j-1]
            degrees[i][j] += prev
        }
    }
    
    for(let i = 0; i <= r; i++){
        for(let j = 1; j <= c; j++){
            let prev = degrees[j-1][i]
            degrees[j][i] += prev
        }
    }
    
    // 스킬 적용
    for(let i = 0; i < c; i++){
        for(let j = 0; j < r; j++){
            if(board[i][j] + degrees[i][j] > 0) answer++;
        }
    }
    return answer;
    
}
