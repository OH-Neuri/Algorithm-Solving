function solution(n, w, num) {
    
    var answer = 0;
    const arr = Array.from({length:Math.ceil(n/w)},()=>[])
    let v = 1
    let c = 0
    for(let i=0;i<arr.length;i++){
       if(i%2==0){
           for(let j=0; j<w; j++){
               if(v==num) c = j
               arr[i][j] = v++;
           }
       }else{
           for(let j=w-1; j>=0;j--){
               if(v==num) c = j
               arr[i][j] = v++;
           }
       }
    }
    
    for(let i=0;i<arr.length;i++){
        if(arr[i][c]>=num && arr[i][c]<=n) answer++;
    }
    
    return answer;
}