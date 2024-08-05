/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function (arr, k) {
    let strCnt = {}
    for (let a of arr) {
        strCnt[a] = (strCnt[a] || 0) + 1
    }
    for (let [str, cnt] of Object.entries(strCnt)) {
        if (cnt == 1) {
            if (k == 1) { return str }
            else { k--; }
        }
    }
    return ""
};