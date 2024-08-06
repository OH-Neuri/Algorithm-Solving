/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function (word) {
    let btn = {}
    for (let str of word) {
        btn[str] = (btn[str] || 0) + 1;
    }
    btn = Object.entries(btn).sort((a, b) => b[1] - a[1])

    let pressCnt = 0
    let result = 0
    for (let i = 0; i < btn.length; i++) {
        result += (btn[i][1] * (parseInt(pressCnt / 8) + 1))
        pressCnt++;
    }

    return result
};
