function solution(topping) {
    // 1) 전체 토핑별 개수가 담긴 Map 객체를 생성한다.
	const map = new Map();
    
    // 2) 형의 토핑의 종류를 담을 Set 객체 생성한다.
    const bro = new Set();
   
    // 3) 형과 동생이 케이크를 공평하게 나누어지는 횟수 
    let answer = 0;

    // 4) Map에 토핑별 개수를 담는다.
    for(let i=0; i<topping.length; i++){
        map.has(topping[i]) ? map.set(topping[i], map.get(topping[i])+1) : map.set(topping[i], 1);
    }
    
    // 5) 토핑의  개수 만큼 반복한다.
    for(let i=0; i<topping.length; i++){
        // 6) Map에 담긴 토핑을 하나씩 빼고 형에게 준다.
        let count = map.get(topping[i])-1;
        bro.add(topping[i]);
        
        // 7) 토핑의 개수가 0이 되면 삭제하고, 남아 있으면 하나씩 뺀다.
        count === 0 ? map.delete(topping[i]) : map.set(topping[i], count);
         
        /* 
        	8) Map에 남아있는 토핑의 종류가 곧 동생의 토핑의 종류이기 때문에  
              형의 토핑의 개수와 동생의 토핑의 개수릴 비교하여 같으면 answer를 증가시킨다.
        */
        if(bro.size === map.size) answer++;

    }
    // 9) 총 공평하게 나누어지는 횟수를 return한다.
    return answer;
}