function solution(n, works) {
    // 남은 작업량이 없는 경우
    if(works.reduce((s,c) =>s+c,0)<=n ) return 0;
    
    let length = works.length
    works.sort((a,b)=>a-b)
    
    while(n){
        let max = works[length-1]
        
        for(let i = length-1; i>=0 ; i--){
            if(works[i]>=max){
                works[i]-=1
                n-=1
            }
            if(!n) break
        }
    }
    return works.reduce((s,c)=> s+(c)**2,0);
}