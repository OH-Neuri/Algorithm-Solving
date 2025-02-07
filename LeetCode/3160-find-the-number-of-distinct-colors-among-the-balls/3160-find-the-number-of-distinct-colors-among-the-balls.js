/**
 * @param {number} limit
 * @param {number[][]} queries
 * @return {number[]}
 */
var queryResults = function(limit, queries) {
    let node = new Map(), color = new Map(), ans = [];

    for (let [x, y] of queries) {
        if (node.has(x)) {
            let prevColor = node.get(x);
            if (prevColor === y) {
                ans.push(color.size);
                continue;
            }
            if (color.get(prevColor) === 1) color.delete(prevColor);
            else color.set(prevColor, color.get(prevColor) - 1);
        }

        node.set(x, y);
        color.set(y, (color.get(y) || 0) + 1);
        ans.push(color.size);
    }

    return ans;
};