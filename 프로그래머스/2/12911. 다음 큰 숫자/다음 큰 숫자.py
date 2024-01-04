def solution(n):
    answer = 0
    # n 다음으로 2진수 1갯수가 똑같은 수
    
    # 방법1 (직관적) 
    # n 1개수 저장
    # n 다음수들 1개수 세서 비교
    bin_cnt = bin(n)[2:].count('1')
    for i in range(n+1,10000001):
        if bin(i)[2:].count('1') == bin_cnt:
            return i
    
    # 방법2 
    # 0,1 규칙찾기
