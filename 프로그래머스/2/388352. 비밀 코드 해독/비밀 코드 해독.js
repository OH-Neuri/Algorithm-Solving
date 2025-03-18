function solution(n, q, ans) {
    var answer = 0;
    const m = q.length
    const arr = Array.from({length:n},(_,i)=>i+1)
    const combination = getCombination(arr, 5)
    
    for(let combIdx = 0; combIdx<combination.length; combIdx++){
        let matched = 0
        for(let i = 0; i < m ; i++){
            let cnt = 0
            const set = new Set(q[i])
            for(let j = 0; j < 5; j++){
                if(set.has(combination[combIdx][j])) cnt++;
            }
            if(ans[i]===cnt) matched++;
        }
        if(matched===m) answer++;
    }
    return answer;
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