function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let dIdx = n - 1;
    let pIdx = n - 1;

    while (dIdx >= 0 || pIdx >= 0) {
       // 가장 먼 거리 찾기
        while (dIdx >= 0 && deliveries[dIdx] === 0) dIdx--;
        while (pIdx >= 0 && pickups[pIdx] === 0) pIdx--;

        if (dIdx < 0 && pIdx < 0) break;

        const dist = Math.max(dIdx, pIdx) + 1;
        answer += dist * 2;

        // cap만큼 배달
        let dCap = cap;
        for (let i = dIdx; i >= 0 && dCap > 0; i--) {
            if (deliveries[i] === 0) continue;
            const deliver = Math.min(deliveries[i], dCap);
            deliveries[i] -= deliver;
            dCap -= deliver;
        }

        // cap만큼 수거
        let pCap = cap;
        for (let i = pIdx; i >= 0 && pCap > 0; i--) {
            if (pickups[i] === 0) continue;
            const pickup = Math.min(pickups[i], pCap);
            pickups[i] -= pickup;
            pCap -= pickup;
        }
    }

    return answer;
}
