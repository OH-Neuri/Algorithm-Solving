function solution(n, works) {
    if(works.reduce((sum,curr,i)=> sum+curr,0)<=n) return 0;
    let sorted = works.sort((a,b)=> a-b)
    const len = works.length
    
    while(n){
        const max = sorted[len-1]
        
        for(let i=len-1;i>=0;i--){
            if(sorted[i]>=max){
                sorted[i]--;
                n--;
            }
            if(!n) break;
        }
    }
    return sorted.reduce((sum,curr,i)=>sum+Math.pow(curr,2),0)
}