function solution(relation) {
    const getCombinations = (arr, num) => { // 조합 구하기
        const combs = [];
        if (num === 1) return arr.map(v => [v]);
        arr.forEach((fixed, index, origin) => {
            const rest = origin.slice(index + 1);
            const combinations = getCombinations(rest, num - 1);
            const attached = combinations.map(v => [fixed, ...v]);
            combs.push(...attached);
        });
        return combs;
    }
    
    let result = 0
    let table = Array.from({length: relation[0].length}, () => [])
    
    // 각 튜플의 속성을 컬럼 배열로 구분
    relation.forEach(r => { 
        for (let ri = 0; ri < r.length; ri += 1) table[ri].push(r[ri])
    })
    // 슈퍼키 제거
    for (let ti = 0; ti < table.length; ti += 1) {
        if (table[ti].length === new Set(table[ti]).size) {
            result += 1
            delete table[ti]
        }
    }
    table = table.filter(t => t)
    if (table.length <= 1) return result
    // 후보키 배열
    const candidate = []
    const tIdx = table.map((t, i) => i)
    for (let i = 2; i <= table.length; i += 1) {
        const combinations = getCombinations(tIdx, i) // 후보키 대상이 될 컬럼 인덱스 조합
        for (const comb of combinations) { 
            let next = false
            // 현재 조합이 이미 후보키에 포함되어있으면(== 최소성을 만족하지 않으면) skip
            for (const cand of candidate) if (cand.every(v => comb.includes(v))) next = true
            if (next) continue
            
            // 컬럼 조합 생성
            const combCheck = []
            for (let j = 0; j < relation.length; j += 1) {
                let combined = ""
                comb.forEach(c => combined += table[c][j])
                combCheck.push(combined)
            }
            if (combCheck.length === new Set(combCheck).size) { // 유일성을 만족하면 후보키에 등록
                result += 1
                candidate.push(comb)
            }
        }
    }
    return result
}