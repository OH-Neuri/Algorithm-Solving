function solution(arr) {
    var answer = [0,0];
    
    const divide = (row, col, len) => {
        
    let dividable = true;
    
    for(let i = row; i < row + len; i++) { 
        for(let j = col; j < col + len; j++) {
            if(arr[row][col] !== arr[i][j]) { // 맨 첫 값과 동일하지않으면
                dividable = false;
            }
        }
    }
    
    let half = Math.floor(len / 2);
        
    if(!dividable) { // 같은 값이 아닐경우
        divide(row, col, half) // 2 quad
        divide(row + half, col, half) // 1 quad
        divide(row, col + half, half) // 3 quad
        divide(row + half, col + half, half) // 4 quad
    }else {
        if(arr[row][col] === 1) answer[1]++;
        else answer[0]++;
    }
}
    
    divide(0, 0, arr.length);
    return answer;
}