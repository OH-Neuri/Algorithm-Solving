const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const dx = [0,-1,0,1]
const dy = [1,0,-1,0]

const [n,k] = input.shift().split(' ').map(Number) //
const [s, x, y] = input.slice(-1)[0].split(" ").map(Number);//
const arr = input.slice(0, -1).map((i) => i.split(" ").map(Number));//
const virusQueue = Array.from({length:k+1}, () =>[])//
const visited = Array.from({length:n},()=> Array.from({length:n},() => false))//

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (arr[i][j] !== 0) {
        visited[i][j] = true;
        virusQueue[arr[i][j]].push([i,j])
    }
  }
}

for(let i=0;i<s;i++){
    for(let j=1;j<=k;j++){
        const nextVirusQueue = [];
        while(virusQueue[j].length){
            const [cx,cy] = virusQueue[j].shift();

            for(let d=0;d<4;d++){
                const [nx,ny] = [cx+dx[d], cy + dy[d]];
                if(nx<0||nx>=n||ny<0||ny>=n) continue;

                if(!visited[nx][ny] && arr[nx][ny]===0){
                    visited[nx][ny] = true
                    arr[nx][ny] = j;
                    nextVirusQueue.push([nx,ny])
                }
            }
        }
        virusQueue[j] = nextVirusQueue
    }
}
console.log(arr[x-1][y-1])

