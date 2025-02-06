/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    const nmap = new Map()
    let answer = 0 

    for(let i=0;i<nums.length;i++){
        for(let j=i+1;j<nums.length;j++){
            let num = nums[i]*nums[j]
            answer += 8* (nmap.get(num)||0)
            nmap.set(num, (nmap.get(num)||0) + 1)
        }
    }
    return answer
};

