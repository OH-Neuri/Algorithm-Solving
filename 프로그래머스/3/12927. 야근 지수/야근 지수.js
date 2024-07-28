function solution(n, works) {
    works = works.sort((a,b)=>a-b)
    let len = works.length
    while(n>0){
        let max = works[len-1]
        let idx = 1
        while(max <= works[len-idx] && n>0){
            n-=1
            works[len-idx] -=1
            if(works[len-idx] ==-1) return 0
            idx +=1
        }
    }
    console.log(works)
    return works.reduce((total,value)=>total + value**2 ,0);
}