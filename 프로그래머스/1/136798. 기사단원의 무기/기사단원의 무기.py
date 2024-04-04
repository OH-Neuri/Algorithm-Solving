def solution(number, limit, power):
    
    answer = 0
    for i in range(1,number+1):
        divisor = []
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                divisor.append(j)
                if j < i//j:
                    divisor.append(i//j)
                if len(divisor) > limit:
                    break
        if len(divisor) > limit:
            answer += power
        else:
            answer += len(divisor)
    return answer