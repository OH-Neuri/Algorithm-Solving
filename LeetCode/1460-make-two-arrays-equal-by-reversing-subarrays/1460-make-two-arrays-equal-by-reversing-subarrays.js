/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    // let len = target.length;
    let targetArr = Array.from({length:Math.max([...target])},()=>0)
    let arrArr = Array.from({length:Math.max([...arr])},()=>0)
    
    console.log(targetArr)
    console.log(arrArr)
    for(let i=0;i<target.length;i++){
        targetArr[target[i]] +=1
        arrArr[arr[i]] +=1
    }

    return targetArr.join() == arrArr.join() ? true : false
};