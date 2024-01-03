def solution(n):
    answer = 0
    sum_list = []
    v = 0
    # 누적합 구하기
    for i in range(n+1):
        v += i
        sum_list.append(v)
    
    start = 0
    end = 1
    answer = 0
    while start < end:
        # 합이 n 작을 경우, end 한칸 이동
        if sum_list[end]-sum_list[start] < n:
            end+=1
        # 합이 n과 같을 경우, start = end, 
        elif sum_list[end]-sum_list[start] == n:
            answer +=1
            start += 1
        else:
            start += 1
    return answer

