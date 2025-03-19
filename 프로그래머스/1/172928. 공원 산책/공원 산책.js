function solution(park, routes) {
    var answer = [];
    let currY = 0
    let currX = 0
    const pr = park.length;
    const pc = park[0].length;
    
    // 시작점찾기
    for(let i=0;i<pr;i++){
        for(let j=0;j<pc;j++){
            if(park[i][j]==="S") {
                currY = i
                currX = j
            }
        }
    }
    
    for(let routeIdx = 0; routeIdx<routes.length; routeIdx++){
        const route = routes[routeIdx].split(" ")
        const op = route[0] // 이동할 방향
        const n = Number(route[1]) // 이동할 칸 수 
        
        let ny = currY 
        let nx = currX
        

        let flag = false 
        for(let i = 0; i < n ;i++){
            if(op==="E") nx++;
            if(op==="S") ny++;
            if(op==="W") nx--;
            if(op==="N") ny--;
            
             // 공원 벗어나거나 장애물 만나면 무시
            if(ny < 0 || ny >= pr || nx < 0 || nx >= pc || park[ny][nx]==="X" ){
                flag = true 
                break;
            }
        }
        
        if(flag) continue
      
        
        //이동
        currY = ny
        currX = nx
    }
        
    return [currY, currX];
}