function solution(sequence, k) {
    let [l, r] = [0, 0]
    let summed = sequence[l] // 현재 쌓여있는 합 (l~r위치 값의 합)
    const candidate = [] // 답안 후보
    while (r < sequence.length) {
        if (summed < k) summed += sequence[++r] // 합이 k보다 작으면 r이동
        else if (summed > k) summed -= sequence[l++] // 합이 k보다 크면 l이동
        else { // 합이 k라면 후보에 넣고 r과 l이동
            candidate.push([l, r])
            summed += sequence[++r]
            summed -= sequence[l++]
        }
    }
    // 후보 중 가장 차가 적은 것을 리턴
    return candidate.sort((a, b) => (a[1] - a[0]) - (b[1] - b[0]))[0] 
}