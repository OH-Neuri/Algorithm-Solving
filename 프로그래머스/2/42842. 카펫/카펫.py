def solution(brown, yellow):
    answer = []
    # 노란색,갈색개수에 맞는 격자크기 구하기
    for i in range(3,20000):
        for j in range(3,200000):
            if i*j > brown+yellow:
                break
            if i*j == brown+yellow and (i-2)*(j-2) == yellow:
                return j,i
