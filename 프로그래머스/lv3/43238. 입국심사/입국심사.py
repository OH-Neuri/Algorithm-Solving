def solution(n, times):
    left, right = min(times), max(times)*n

    while left <= right:
        mid = (left + right) // 2
        check = 0
        for x in times:
            check += mid//x
            if check >=n:
                break
        
        if check >=n:
            answer = mid
            right = mid -1
        elif check <n:
            left = mid +1
            
    return answer