/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    let len = target.length;
    let targetArr = Array.from({length:len},()=>0)
    let arrArr = Array.from({length:len},()=>0)
    for(let i=0;i<len;i++){
        targetArr[target[i]] +=1
        arrArr[arr[i]] +=1
    }
    return targetArr.join() == arrArr.join() ? true : false
};