def solution(cap, n, deliveries, pickups):
    # 가는 길에 택배 주고 수거까지 해야 효율적
    # 배달이 0이면 cap만큼 수거
    # 수거가 0이면 cap만큼 배달
    # 끝에 계속 확인해야함
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    
    deli = 0
    pick = 0
    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer +=(n-i)*2
    
    return answer