function solution(word) {
    const vowels = ['A', 'E', 'I', 'O', 'U'];
    const counts = [781, 156, 31, 6, 1]; // 각 자리수별 가능한 단어 수
    
    let answer = 0;
    for (let i = 0; i < word.length; i++) {
        answer += vowels.indexOf(word[i]) * counts[i] + 1; // 해당 자리의 알파벳 인덱스에 따른 영향을 더해줌
    }
    
    return answer;
}