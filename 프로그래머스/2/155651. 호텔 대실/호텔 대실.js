function solution(book_time) {
    return book_time.sort().reduce((acc, cur) => {
        const [startTime, endTime] = [convertMinFromStringTime(cur[0]), convertMinFromStringTime(cur[1]) + 10];
        
        const idx = acc.findIndex(x => x <= startTime);
        
        if(idx === -1) {
            acc.push(endTime)
        } else {
            acc[idx] = endTime;
        }
        return acc;
    }, []).length;
}

function convertMinFromStringTime(strTime) {
    const [h, m] = strTime.split(":");
    return Number(h) * 60 + Number(m);
}