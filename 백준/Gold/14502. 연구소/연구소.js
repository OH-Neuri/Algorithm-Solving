const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

let dx = [0,-1,0,1]
let dy = [1,0,-1,0]

const [n, m] = input.shift().split(' ').map(Number);
let matrix = input.map((line)=>line.split(" ").map(Number))
let virus = [];

for(let i=0; i<n;i++){
    for(let j=0;j<m;j++){
        if (matrix[i][j] === 2) virus.push([i, j]);
    }
}

const countSafeZone = (tmpMap) =>{
    let sum = 0
    for(let i=0;i<n;i++){
        for(let j=0;j<m;j++){
            if (tmpMap[i][j] === 0) sum += 1;
        }
    }
    return sum
};

const moveVirus = (queue,tmpMap) =>{
    while (queue.length > 0) {
        let [x, y] = queue.shift();
        for (let k = 0; k < 4; k++) {
            let nx = x + dx[k];
            let ny = y + dy[k];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && tmpMap[nx][ny] === 0) {
                tmpMap[nx][ny] = 2
                queue.push([nx,ny])
            }
        }
    }
    return tmpMap
}

let answer = 0
const DFS = (depth) => {
    if(depth===3){
        answer = Math.max(answer, countSafeZone(moveVirus([...virus], matrix.map(v=>[...v]))));
        return 
    }
    
    for(let i = 0; i<n; i++){
        for(let j = 0; j<m; j++){
            if (matrix[i][j] === 0) {
                matrix[i][j] = 1;
                DFS(depth+1)
                matrix[i][j] = 0;
            }
        }
    }
}
DFS(0)
console.log(answer)