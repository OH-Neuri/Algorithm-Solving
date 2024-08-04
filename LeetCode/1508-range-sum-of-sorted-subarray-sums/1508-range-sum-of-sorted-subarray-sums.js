/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    let len = nums.length
    let sum = 0
    let arr = []
    for(let i=0; i<len; i++){
        sum = 0
        for(let j=i; j<len; j++){
            sum += nums[j]
            arr.push(sum)
        }
    }
    arr.sort((a,b)=>a-b)
    return arr.reduce((total, value, idx)=> {
        if(idx >= left-1 && idx <= right-1){
            return total+value;
        }
        return total;
        },0)%(10**9+7)

};