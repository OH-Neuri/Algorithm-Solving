function solution(cacheSize, cities) {
    const city = cities.map(a => a.toLowerCase()); 
    // 배열 내 요소 소문자로
    
    let queue = [];
    let time = 0;
    
    for(let i = 0; i < city.length; i++){
        if(!queue.includes(city[i])){ // 큐에 도시가 존재하지 않으면
            time+=5;
            queue.push(city[i]);
            if(queue.length > cacheSize){ // 캐시사이즈를 넘으면 앞 요소 삭제
                queue.shift();
            }
        }
        else{ // 도시가 큐에 있으면
            time++;
            let idx = queue.indexOf(city[i]); 
            queue.splice(idx, 1);
            queue.push(city[i]); // 인덱스 찾아서 제거 후 맨 뒤에 삽입
        }
    }
    return time;
}