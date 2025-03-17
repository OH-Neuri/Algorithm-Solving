function solution(points, routes) {
    let answer = 0
    
    let routesLen = routes.length
    const shortestPath = Array.from({length:routesLen}, () => []) // 로봇들의 최단경로들
    let shortestPathLongestLen = 0
    
    for(let routeIndex = 0; routeIndex < routesLen; routeIndex++){
        const route = routes[routeIndex];
       
        
        for(let i = 1; i < route.length; i++){
            const startPointsIdx = route[i-1]-1
            const endPointsIdx = route[i]-1

            const startToEnd = [
                points[startPointsIdx][0]-1, points[startPointsIdx][1]-1, 
                points[endPointsIdx][0]-1, points[endPointsIdx][1]-1
            ]
            const posPath = findPath(...startToEnd)
            shortestPath[routeIndex].push(...posPath)
        }
        const endPoints = [points[route[route.length-1]-1][0]-1,points[route[route.length-1]-1][1]-1]
        shortestPathLongestLen = Math.max(shortestPathLongestLen,shortestPath[routeIndex].length)
        shortestPath[routeIndex].push([endPoints[0],endPoints[1]])
    }

    for(let i = 0; i <= shortestPathLongestLen+1; i++ ){
        const pMap = new Map()
        for(let j=0; j < routes.length; j++){
            if(!shortestPath[j][i]) continue
            const pos = `${shortestPath[j][i]}`
            pMap.set(pos, (pMap.get(pos)||0)+1)
            
            if(pMap.get(pos)===2) answer++;
        }
    }
    
    return answer;
}

function findPath(r1, c1, r2, c2){
    const tmp = []
    
    if(r1!==r2){
        const rDiff = Math.abs(r1-r2)
        if(r1>r2){
            for(let i=0;i<rDiff;i++){
                tmp.push([r1-i,c1])
            }
        }else{
            for(let i=0;i<rDiff;i++){
                tmp.push([r1+i,c1])
            }
        }
    }
    
     if(c1!==c2){
        const cDiff = Math.abs(c1-c2)
        if(c1>c2){
            for(let i=0;i<cDiff;i++){
                tmp.push([r2,c1-i])
            }
        }else{
            for(let i=0;i<cDiff;i++){
                tmp.push([r2,c1+i])
            }
        }
    } 
    return tmp
}