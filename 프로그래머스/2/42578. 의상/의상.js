function solution(clothes) {
    const clothesMap = {};
    let answer = 1;
    clothes.forEach(arr => {   
        const [type, name] = arr;
        if(clothesMap.hasOwnProperty(name)) {	
            clothesMap[name]++;    	
        }
        else {
            clothesMap[name] = 1;  
        }
    })
    for(const key in clothesMap) {
        answer *= (clothesMap[key] + 1);		
    }
    return answer - 1;
}