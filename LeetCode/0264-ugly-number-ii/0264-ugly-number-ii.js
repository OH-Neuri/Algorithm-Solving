/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function (n) {
    if(n===1) return 1

    let uglyNumberCnt = 1
    let uglyNumber = [2, 3, 5]
    for (let i = 2; i <= 1000000000; i++) {
        let num = i
        for (let ugly of uglyNumber) {
            while (num % ugly === 0) {
                num /= ugly
            }
        }
        if (num === 1) uglyNumberCnt += 1
        if (uglyNumberCnt === n) return i
    }
};