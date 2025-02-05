/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    
    let len = s1.length;
    let answer = false
    for(let i=0;i<len;i++){
        for(let j=0;j<len;j++){
            let tmp = [...s2]
            if(i!==j){
                tmp[i] = s2[j]
                tmp[j] = s2[i]
            }
            if(s1==tmp.join("")) answer = true
        }
    }
    return answer
};

// 문자열 비교