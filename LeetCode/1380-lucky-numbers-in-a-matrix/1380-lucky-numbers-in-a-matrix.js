/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers  = function(matrix) {
    
    let arrCloumn = Array.from({length:matrix[0].length},()=>-1) // 인덱스 
    let result = []
    for(let j=0; j<matrix[0].length;j++){ 
        let maxClomunValue = -1 
        for(let i=0;i<matrix.length;i++){ 
            if(maxClomunValue < matrix[i][j]) { 
                maxClomunValue = matrix[i][j]
                arrCloumn[j] = i
            }
        }    
        let minRowValue = Math.min(...matrix[arrCloumn[j]]) // 열 최솟값
        if(j == matrix[arrCloumn[j]].indexOf(minRowValue)) {
            result.push(minRowValue)
        }
    }
    return result
};