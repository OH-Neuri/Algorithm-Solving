function solution(n) {
    let cnt=0;
    for(let i=1;i*i<n;i++){
        if(n%i==0) cnt++;
    }
    console.log(Math.sqrt(n))
    return (Math.sqrt(n))%1==0?cnt*2+1:cnt*2;
}