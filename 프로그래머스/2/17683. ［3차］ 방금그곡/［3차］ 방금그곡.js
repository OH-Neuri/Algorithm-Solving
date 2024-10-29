function solution(m, musicinfos) {
    const normalize = (melody) => {
        return melody.replace(/([A-Z])#/g, (_, group) => group.toLowerCase());
    };
    
    const getMin = (time) => {
        const [hour, minute] = time.split(':').map(Number);
        return hour * 60 + minute;
    };
    
    const getDiff = (start, end) => {
        return getMin(end) - getMin(start);
    };
    
    const music = musicinfos.map(info => {
        const [start, end, title, melody] = info.split(',');
        return {
            time: getDiff(start, end),
            title,
            melody: normalize(melody)
        };
    });
    
    const targetMelody = normalize(m);
    let output = { title: '(None)' };
    music.forEach(info => {
        const { time, title, melody } = info;
        let compMelody = melody.repeat(2);
        let count = 2;
        while (targetMelody.length + melody.length - 1 > compMelody.length) {
            compMelody += melody;
            count++;
        }
        const index = compMelody.indexOf(targetMelody);
        if (index >= 0 && index + targetMelody.length <= time) {
            if (output.title === '(None)' || output.time < time) {
                output = info;
            }
        }
    });
    return output.title;
}