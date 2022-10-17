import java.util.*;
class Solution {
    static int MIN_TIME,MIN_COST,TIME_PER,COST_PER;
    public int[] solution(int[] fees, String[] records) {
        int[] answer;
        MIN_TIME = fees[0];
        MIN_COST = fees[1];
        TIME_PER = fees[2];
        COST_PER = fees[3];
        // 차들의 입출차 확인 
        // 차량 번호, 시간
        Map<String, Integer> parkingLot = new HashMap<>();
        // 차들의 누적 주차 시간
        // 차량 번호, 누적 간
        Map<String, Integer> total = new TreeMap<>();

        for (String record : records) {
            String[] values = record.split(" ");
            String[] timeSplit = values[0].split(":");
            String carNumber = values[1];
            String status = values[2];

            int time = (Integer.parseInt(timeSplit[0]) * 60) + Integer.parseInt(timeSplit[1]);

            // 입차
            if (status.equals("IN")) {
                parkingLot.put(carNumber, time);
            }
            //출차
            else {
                int parkingTime = (time - parkingLot.get(carNumber));
                total.put(carNumber, total.getOrDefault(carNumber, 0) + parkingTime);
                parkingLot.remove(carNumber);
            }
        }
        //출차 안한 차
        // 23:59분에서 입차한 시간 빼서 total에 넣어준다.
        if (!parkingLot.isEmpty()) {
            int lastTime = (23 * 60) + 59;
            for (String key : parkingLot.keySet()) {
                int time = lastTime - parkingLot.get(key);
                total.put(key, total.getOrDefault(key, 0) + time);
            }
        }
        
        // total에 저장된 각 차들의 누적 주차 시간들로 주차 요금 계산
        answer = new int[total.size()];
        int idx = 0;
        for (String keys : total.keySet()) {
            int totalTime = total.get(keys);
            int result = MIN_COST;
            if (totalTime > MIN_TIME) {
                totalTime -= MIN_TIME;
                result += ((totalTime / TIME_PER) * COST_PER);
                if (totalTime % TIME_PER > 0) result += COST_PER;
            }
            answer[idx++] = result;
        }

        return answer;
    }
}