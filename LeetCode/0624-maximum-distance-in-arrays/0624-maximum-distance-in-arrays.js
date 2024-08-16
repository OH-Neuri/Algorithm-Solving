/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function (arrays) {
    let sortedMaxValue = Object.entries(arrays).sort((a, b) => b[1][b[1].length - 1] - a[1][a[1].length - 1])
    let maxValue = [[sortedMaxValue[0][0], sortedMaxValue[0][1][sortedMaxValue[0][1].length - 1]], [sortedMaxValue[1][0], sortedMaxValue[1][1][sortedMaxValue[1][1].length - 1]]]
    let sortedMinValue = Object.entries(arrays).sort((a, b) => (a[1][0]) - (b[1][0]))
    let minValue = [[sortedMinValue[0][0], sortedMinValue[0][1][0]], [sortedMinValue[1][0], sortedMinValue[1][1][0]]]

    if (maxValue[0][0] !== minValue[0][0]) return Math.abs(maxValue[0][1] - minValue[0][1])
    return Math.max(Math.abs(maxValue[1][1] - minValue[0][1]), Math.abs(maxValue[0][1] - minValue[1][1]))
};