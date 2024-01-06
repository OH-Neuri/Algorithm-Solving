import math
def solution(fees, records):
    answer = []
    car_time = {}
    
    for car_record in records:
        car_record = car_record.split(" ")
        time = car_record[0] # 시간
        num = car_record[1] # 차량 번호
        info = car_record[2] # 입출차 정보
        
        # 입차한 경우
        if info == 'IN':
            if num not in car_time.keys():
                car_time[num] = (time, 0) # 입차시간, 사용시간
            else:
                car_time[num] = (time, car_time[num][1])
                
        # 출차한 경우
        if info == 'OUT':

            # 시간계산
            tmp = car_time[num][0].split(':')
            in_time = int(tmp[0])*60 + int(tmp[1])
            tmp = time.split(':')
            out_time = int(tmp[0])*60 + int(tmp[1])
            result_time = out_time - in_time

            # 나감처리
            car_time[num] = (False, car_time[num][1]+result_time)

    # 출차된 내역이 없는 차량 요금
    for no_out in car_time.keys():
        if car_time[no_out][0]:
            # 시간 계산
            tmp = car_time[no_out][0].split(':')
            in_time = int(tmp[0])*60 + int(tmp[1])
            out_time = 23*60 + 59
            result_time = out_time - in_time
            car_time[no_out] = (False, car_time[no_out][1] + result_time)
            
    
    car_numbers = sorted(car_time)
    for car_num in car_numbers:
        result_time = car_time[car_num][1]
        # 기본요금
        if result_time <=fees[0]:
            answer.append(fees[1])
        # 추가요금 
        else:
            answer.append(fees[1]+ math.ceil((result_time-fees[0])/fees[2]) * fees[3])
        
    return answer