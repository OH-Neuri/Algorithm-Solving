function solution(board, moves) {
    var answer = 0;
    const stack = []
    const bRow = board.length
    const bCol = board[0].length
    const boardArr = Array.from({length:bCol}, () => [])
    
    for(let i = 0; i < bCol; i++){
        for(let j = bCol - 1; j >= 0; j--){
            if(!board[j][i]) break;
            boardArr[i].push(board[j][i])
        }
    }


    for(let move of moves){
        const lastNum = boardArr[move - 1].pop()
        if(lastNum) stack.push(lastNum)
        
        let stackLen = stack.length
        while(stack.length >= 2 && stack[stackLen - 1] == stack[stackLen - 2]){
            stack.pop()
            stack.pop()
            answer += 2
            stackLen = stack.length
        }
    }

    return answer;
}