/**
 * @param {number[][]} grid
 * @return {number}
 */
var equalPairs = function(grid) {
    
    let answer = 0
    let len = grid.length
    for(let i=0; i<len; i++){
        let row = grid[i]
        for(let j=0; j<len ;j++){
            let col = []
            for(let l=0; l<len; l++){
               col.push(grid[l][j])
            }   
            console.log(col)
        if(JSON.stringify(row)==JSON.stringify(col)) answer++;
        }
    }
    return answer
};