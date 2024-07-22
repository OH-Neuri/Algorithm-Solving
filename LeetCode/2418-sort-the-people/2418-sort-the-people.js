/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let sortedName = []
    let result = []

    for(let i=0;i<names.length;i++){
        sortedName.push({heights:heights[i], idx:i})
    }
    sortedName.sort((a,b)=>b.heights - a.heights)
    for(let {height, idx} of sortedName){
        result.push(names[idx])
    }

    return result
};