function solution(routes) {
    var answer = 0;
    routes = routes.sort((a,b)=>{
        if(a[0]==b[0]) return a[1]-b[1]
        return a[0]-b[0]
    })
    
    let s = -30002
    let e = -30001
    
    for(let [start, end] of routes){
        if(e < start){
            answer++
            s = start
            e = end
        }else{
            s = start
            e = Math.min(end,e)
        }
    }
    return answer;
}