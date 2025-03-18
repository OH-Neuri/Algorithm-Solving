function solution(relation) {
    const colLen = relation[0].length;
    const columnArr = Array.from({length:colLen}, (_,i)=>i);
    let candidateKeys = [];
    
    for(let r = 1; r <= colLen; r++){
        const combinations = getCombination(columnArr,r)
        for(let candidate of combinations){
            if(isUnique(relation, candidate) && isMinimal(candidate, candidateKeys)){
                candidateKeys.push(candidate)
            }
        }
    }
    
    return candidateKeys.length;
}

// 최소성 확인
function isMinimal(candidate, selectedKeys){
    for(let key of selectedKeys){
        if(key.every(col => candidate.includes(col))) return false
    }
    return true
}

// 유일성 확인
function isUnique(relation, columns){
    const seen = new Set();
    for(let row of relation){
        const key = columns.map(col => row[col]).join(",");
        if(seen.has(key)) return false;
        seen.add(key)
    }
    return true;
}


function getCombination(arr, selectNumber){
    const result = []
    const n = arr.length;
    
    function dfs(start, path){
        if(path.length=== selectNumber){
            result.push([...path]);
            return 
        }
        
        for(let i = start; i<n; i++){
            path.push(arr[i]);
            dfs(i+1, path);
            path.pop()
        }
    }
    dfs(0,[]);
    return result 
}