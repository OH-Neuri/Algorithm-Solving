function solution(cacheSize, cities) {
    const cache = []
    var answer = 0;
    
    for(let city of cities){
        // 대소문자 구분 없음
        city = city.toLowerCase() 
        
        const idx = cache.indexOf(city)
        
        // cache hit
        if(idx!==-1){
            cache.splice(idx,1) // 해당 도시 제거
            cache.push(city) // 뒤에 추가
            answer+=1            
        }else{ 
        // cache miss
            // cache에 빈 공간이 없는 경우,
            if(cacheSize && cache.length >= cacheSize){
                cache.shift() // 가장 오래된 도시 제거
            }
            
            // cahce에 도시 넣기
            if(cacheSize) cache.push(city)
            answer += 5            
        }
    }
    
    return answer;
}