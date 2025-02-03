/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    
    let tmp = nums[0]
    let iCnt = 0
    let dCnt = 0
    let answer = 0

    for(let i = 1; i<nums.length;i++){
        if(tmp<nums[i]){         //감소
            iCnt+=1
        }else{
            iCnt = 0
        }

        if(tmp>nums[i]){   //증가
            dCnt +=1
        }else{
            dCnt = 0
        }
        answer = Math.max(answer,Math.max(iCnt, dCnt))
        tmp = nums[i]
    }
    return answer + 1
};