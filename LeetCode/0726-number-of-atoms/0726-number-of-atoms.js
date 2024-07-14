function countOfAtoms(formula) {
    let stack = [{}];
    let i = 0;
    const n = formula.length;
    while (i < n) {
        if (formula[i] === '(') {
            stack.push({});
            i += 1;
        } else if (formula[i] === ')') {
            let top = stack.pop();
            i += 1;
            let i_start = i;
            while (i < n && isDigit(formula[i])) {
                i += 1;
            }
            let multiplier = parseInt(formula.slice(i_start, i) || 1, 10);
            for (let element in top) {
                if (top.hasOwnProperty(element)) {
                    stack[stack.length - 1][element] = (stack[stack.length - 1][element] || 0) + top[element] * multiplier;
                }
            }
        } else {
            let i_start = i;
            i += 1;
            while (i < n && isLower(formula[i])) {
                i += 1;
            }
            let element = formula.slice(i_start, i);
            i_start = i;
            while (i < n && isDigit(formula[i])) {
                i += 1;
            }
            let count = parseInt(formula.slice(i_start, i) || 1, 10);
            console.log(count)
            stack[stack.length - 1][element] = (stack[stack.length - 1][element] || 0) + count;
        }
    }

    let result = stack.pop();
    let sortedElements = Object.keys(result).sort();
    return sortedElements.map(element => `${element}${result[element] > 1 ? result[element] : ''}`).join('');
}

function isDigit(char) {
    return char >= '0' && char <= '9';
}

function isLower(char) {
    return char >= 'a' && char <= 'z';
}

