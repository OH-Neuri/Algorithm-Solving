def solution(k, ranges):
    answer = []
    hail_arr = [k]
    # 우박수열 만들기
    while k>1:
        if k%2==0:
            k//=2
        else:
            k=k*3+1
        hail_arr.append(k)
        
    for a, b in ranges:
        if b<=0: # [a,-b]인 경우
            b = len(hail_arr) -1 + b
        
        if a>b: # 유효하지 않은 구간일 경우
            answer.append(-1.0)
            continue
        
        h = max(hail_arr[a:b+1]) # 사각형 높이
        area = (b-a) * h
        for i in range(a,b):
            area -= 1 * abs(hail_arr[i]-hail_arr[i+1]) / 2 # 빈 공간 삼각형 제거
            area -= (h-max(hail_arr[i],hail_arr[i+1])) * 1 # 빈 공간 사각형 제거
        answer.append(area)
            
    return answer