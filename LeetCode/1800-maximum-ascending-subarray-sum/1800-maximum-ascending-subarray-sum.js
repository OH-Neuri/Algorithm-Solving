/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    
    let answer = 0
    let flag = false
    let sum = 0
    for(let i=1;i<nums.length;i++){
        if(nums[i-1]<nums[i]){
            if(!flag) { 
                sum+=nums[i-1]
                flag = true
            }
            sum+=nums[i]
        }else{
            flag=false
            sum=0
        }
        answer = Math.max(answer,sum)
    }
    return answer
};