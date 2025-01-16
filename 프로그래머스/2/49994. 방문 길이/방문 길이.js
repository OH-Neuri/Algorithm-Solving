function solution(dirs) {
    const move = { U: [0, 1], D: [0, -1], R: [1, 0], L: [-1, 0] };
    let cur = [0, 0];
    const moveList = new Set();
    
    for (const dir of dirs) {
        const nextX = cur[0] + move[dir][0];
        const nextY = cur[1] + move[dir][1];
        
        if (nextX > 5 || nextX < -5 || nextY > 5 || nextY < -5) continue;
        
        moveList.add(`${cur[0]}${cur[1]}${nextX}${nextY}`);
        moveList.add(`${nextX}${nextY}${cur[0]}${cur[1]}`);
        
        cur = [nextX, nextY];
    }
    
    return moveList.size / 2;
}