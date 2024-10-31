function solution(name) {
    let answer = 0;
    const min = 65; //A의 아스키코드
    const max = 90 + 1; //Z의 아스키코드 + A->Z로 가는 횟수 1회
    
    const findChar = (find) => {
        //A에서 특정 문자로 가는 최소 거리
        const findCode = find.charCodeAt(); //찾고자하는 문자의 아스키코드
        return Math.min(findCode - min, max - findCode);
    }
    
    const chars = name.split('').map((c) => findChar(c));
    let minMove = chars.length - 1;
    
    chars.forEach((char, idx) => {
        answer += char;
        
        let cursor = idx + 1;
        while(cursor < chars.length && chars[cursor] === 0) cursor++;
        
        minMove = Math.min(minMove, //정 방향으로 전진
                          (idx * 2) + chars.length - cursor, //뒤로 돌아가기
                          idx + 2 * (chars.length - cursor)); //뒤의 요소를 먼저 입력하기
    })
    
    return answer + minMove;
}