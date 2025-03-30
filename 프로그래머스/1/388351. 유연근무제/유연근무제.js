function solution(schedules, timelogs, startday) {
    const len = timelogs.length;
    const reward = Array.from({ length: len }, () => true);
    let currDay = startday;

    for (let i = 0; i < 7; i++) {
        if (currDay >= 6) {
            // 주말은 검사 대상이 아님
            currDay = currDay % 7 + 1;
            continue;
        }

        for (let employee = 0; employee < len; employee++) {
            const schedule = schedules[employee];
            const scheduleHour = Math.floor(schedule / 100);
            const scheduleMin = schedule % 100;

            // 출근 마감 시간 = 근무 시작 시간 + 10분
            let totalMinutes = scheduleHour * 60 + scheduleMin + 10;
            const passHour = Math.floor(totalMinutes / 60);
            const passMin = totalMinutes % 60;
            const passTime = passHour * 100 + passMin;

            const logTime = timelogs[employee][i];
            if (logTime === -1 || logTime > passTime) {
                reward[employee] = false;
            }
        }

        currDay = currDay % 7 + 1; // 요일 증가 (1~7)
    }

    return reward.filter(Boolean).length;
}
