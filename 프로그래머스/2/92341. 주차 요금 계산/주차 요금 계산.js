function solution(fees, records) {
  const parking = {};

  records.forEach((v) => {
    const [time, id, status] = v.split(" ");
    const [hour, minute] = time.split(":");
    // time을 분으로 통일
    const replaceTime = hour * 60 + +minute;

    // Object에 입고할 차량이 없다면 등록
    if (!parking[id]) {
      parking[id] = { time: 0, id };
    }

    // 현재 상태 기록
    parking[id].status = status;

    // 마지막으로 입고한 시간 기록
    if (status === "IN") {
      parking[id].lastInTime = replaceTime;
      return;
    }

    // 주차 시간에 += (현재 입고 시간 - 마지막 입고 시간)
    parking[id].time += replaceTime - parking[id].lastInTime;
  });

  // 차량 번호가 낮은 순서로 비용 return
  return Object.values(parking)
    .sort((a, b) => a.id - b.id)
    .map((v) => {
      // 최대 시간은 24 * 60 -1 = 1439 (분)
      if (v.status === "IN") v.time += 1439 - v.lastInTime;
      // 기본 시간 이내라면 기본 요금
      if (fees[0] > v.time) return fees[1];
      // 기본 요금 + (( 주차 시간 - 기본 시간 ) / 단위 시간) * 요금
      return fees[1] + Math.ceil((v.time - fees[0]) / fees[2]) * fees[3];
    });
}