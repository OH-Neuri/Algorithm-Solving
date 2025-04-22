// 조합 numberC3 -> 합찾기
function solution(number) {
    let answer = 0
    var combList = getComb(number,3)
    
    for(let comb of combList){
        const num1 = comb[0]
        const num2 = comb[1]
        const num3 = comb[2]
        if(num1 + num2 + num3 === 0) answer++;
    }
    return answer;
}

function getComb(arr, selectNum){
    const result = [];
    const n = arr.length;
    
    function dfs(start, path){
        if(path.length==selectNum){
            result.push([...path])
            return;
        }
        
        for(let i = start; i < n; i++){
            path.push(arr[i])
            dfs(i + 1, path);
            path.pop()
        }
    }
    
    dfs(0, [])
    return result;
}