function solution(operations) {
    const heap = [];
    const op = operations.map(operation => operation.split(' '));
  	// 입력된 명령어를 공백(' ')을 기준으로 분할한다.
  	// 따라서 배열[0] = 명령어, 배열[1] = 숫자로 접근할 수 있다.
    
    op.forEach(num => {
        if(num[0] === 'I') {	// 명령어가 I라면 데이터 삽입
            heap.push(Number(num[1]))
        }
        else {	// 그 외의 경우, 즉 명령어가 D인 경우
            const findValue = (num[1] === '1' ? Math.max : Math.min)(...heap);
            const delIdx = heap.indexOf(findValue);
            heap.splice(delIdx, 1);
        }
    })
    
    return heap.length ? [Math.max(...heap), Math.min(...heap)] : [0, 0];
}