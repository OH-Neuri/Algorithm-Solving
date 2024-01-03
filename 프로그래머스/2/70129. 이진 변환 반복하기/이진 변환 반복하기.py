def solution(s):
    answer = []
    zero_cnt = 0
    work_cnt = 0
    l = 0

    while s != '1':
        # 제거할 0의 개수
        zero_cnt += s.count('0')
        # 0 제거 후 길이
        l = len(s.replace('0',''))
        # 이진 변환 결과
        s = bin(l)[2:]
        work_cnt +=1
        
    return [work_cnt, zero_cnt]

