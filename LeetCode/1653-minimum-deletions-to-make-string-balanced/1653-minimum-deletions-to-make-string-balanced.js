/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function (s) {
    let start = 0
    let end = s.length - 1
    while (s[start] == "a") {
        start++;
    }
    while (s[end] == "b") {
        end--;
    }

    let aCnt = 0
    let bCnt = 0
    for (let i = start; i <= end; i++) {
        console.log(s[i])
        if (s[i] == "a") {
            aCnt++
        } else {
            bCnt++;
        }
    }
    return Math.min(aCnt, bCnt)
};