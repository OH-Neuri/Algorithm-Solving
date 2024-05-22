function solution(maps) {
    var n = maps.length; // 행
    var m = maps[0].length; // 열
    var dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]; // 상하좌우

    // bfs
    var bfs = () => {
        var queue = [[0, 0, 1]]; // 행, 열, 이동거리
        maps[0][0] = 0; // 이동한 거리 0으로 막기

        while (queue.length > 0) {  //큐가 비어있지 않는 동안 반복
            var [row, col, distance] = queue.shift();

            if (row == n - 1 && col == m - 1) {
                return distance;
            }

            for (var [r, c] of dir) {
                var newRow = row + r;
                var newCol = col + c;   //현재 위치에서 상하좌우로 이동한 새로운 위치

                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && maps[newRow][newCol] === 1) {
                    queue.push([newRow, newCol, distance + 1]);
                    maps[newRow][newCol] = 0; // 방문한 위치를 0으로 표시
                }
            }
        }
        return -1;
    };

    return bfs();
}