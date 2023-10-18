def solution(n, t, m, p):
    answer = "0"
    notation = "0123456789ABCDEF"

    for num in range(1, m * t): 
        result = ""
        while num > 0: 
            num, remainder = divmod(num, n)
            result += notation[remainder] 

        answer += result[::-1]
    return answer[p-1::m][:t]
