const solution = (elements) => {
    const sumSet = new Set();
    
    const len = elements.length;
    for (let i=1; i<=len; i++) { // 연속 부분 수열의 길이
        let sum = 0;
        for (let j=0; j<len; j++) { // 연속 부분 수열 시작 지점의 인덱스
            if (j === 0) { // 최초 한 번의 창문에 대해서만 직접 합을 구하기
                for (let k=0; k<i; k++) {
                    sum += elements[k];
                }
            }
            else { // 이후 창문들에 대해서는 이전에 구한 합을 활용하기
                sum -= elements[j-1];
                sum += elements[(j+i-1) % len];
            }
            sumSet.add(sum);
        }
    }
    
    return sumSet.size;
}