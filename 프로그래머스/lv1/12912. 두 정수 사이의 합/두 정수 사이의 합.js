function solution(a, b) {
    let sum=0;
    if(a-b<0){
        for(let i=a;i<=b;i++){
            sum+=i;
        }
    }else{
        for(let i=b;i<=a;i++){
            sum+=i
        }
    }
    return sum;
}