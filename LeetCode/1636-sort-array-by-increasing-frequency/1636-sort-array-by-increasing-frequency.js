/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    // 객체에 담기
    let countNums = {}
    nums.forEach(n=>{
        if(countNums[n]){
            countNums[n] ++;
        }else{
            countNums[n] =1
        }
    })
    // 정렬하기
    countNums = Object.entries(countNums)
    countNums.sort((a,b)=>{if(a[1]!==b[1]) return a[1]-b[1] 
    if(a[1]==b[1]) return b[0]-a[0]})

    let result = []
    for(let [num, count] of countNums){
        for(let i=0;i<count;i++){
            result.push(parseInt(num))
        }
    }
    return result
};