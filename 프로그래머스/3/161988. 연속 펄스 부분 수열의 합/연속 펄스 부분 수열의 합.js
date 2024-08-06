function solution(sequence) {
    var answer = 0;
    let seq1 = sequence.map((v, i) => (i % 2 === 0 ? v : -v));
    let seq2 = sequence.map((v, i) => (i % 2 === 0 ? -v : v));
    return Math.max(sum(seq1),sum(seq2))
}

function sum(arr){
 let maxSoFar = 0; // 현재까지 최대 서브어레이 합
    let currentMax = 0; // 현재 서브어레이 합

    for (let i = 0; i < arr.length; i++) {
        // 현재 요소를 추가하여 서브어레이 합 갱신
        currentMax = Math.max(arr[i], currentMax + arr[i]);
        
        // 현재까지 최대 서브어레이 합 갱신
        maxSoFar = Math.max(maxSoFar, currentMax);
    }
    return maxSoFar;
    
}