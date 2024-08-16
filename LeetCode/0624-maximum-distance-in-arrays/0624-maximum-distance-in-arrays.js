/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function (arrays) {
    let minValue = arrays[0][0]
    let maxValue = arrays[0][arrays[0].length-1]
    let result = 0
    for(let i=1; i<arrays.length; i++){
        let currentMin = arrays[i][0]
        let currentMax = arrays[i][arrays[i].length-1]

        result = Math.max(result, Math.max(Math.abs(maxValue-currentMin), Math.abs(currentMax-minValue)))
        maxValue = Math.max(maxValue, currentMax)
        minValue = Math.min(minValue, currentMin)
    }
    return result
};