function solution(cap, n, deliveries, pickups) {
    let answer = 0;
  	// deliveries[i]와 pickups[i]가 둘 다 0일 경우 방문할 필요 없으므로 처음부터 제거해주기. 
   	for(let i=n-1; i>=0; i--){
        if(deliveries[i] === 0 && pickups[i] === 0) {
            deliveries.pop();
            pickups.pop();
        } else break;
    }
    
    let [dLen, pLen] = [deliveries.length-1, pickups.length-1];
  	// 배달과 수거를 모두 끝낼 때까지 반복
    while(dLen >= 0 || pLen >= 0){
        let max = Math.max(dLen, pLen);
        answer += (max+1)*2;
        dnp(dLen,cap,deliveries);
        dnp(pLen,cap,pickups);
        [dLen, pLen] = [deliveries.length-1, pickups.length-1];
    }
    
    return answer;
}

function dnp(n,cap,arr){
    let count = 0;
    for(let i=n; i>=0; i--){
      	// 트럭에 다 실을 수 있는 경우
        if(cap-count >= arr[i]) {
            count += arr[i];
            arr.pop();
        }
      	// 일부만 실을 수 있는 경우
      	else {
            arr[i] -= cap-count;
            return;
        }
    }
}