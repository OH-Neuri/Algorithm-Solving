/**
 * @param {string} target
 * @return {number}
 */
var minFlips = function(target) {
    let isFlipped = false;
    let count = 0;
    for(let i = 0; i < target.length ; i++){
        if(target[i] == 1 && !isFlipped){
            count++;
            isFlipped = true;
        }else if(target[i] == 0 && isFlipped){
            count++
            isFlipped = false;
        }
    }

    return count
};