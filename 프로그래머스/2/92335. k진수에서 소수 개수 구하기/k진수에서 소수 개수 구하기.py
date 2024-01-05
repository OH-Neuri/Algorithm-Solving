import math
import re
def solution(n, k):
    answer = 0
    
    # n을 k진법으로 변환
    def convert(n, base):
        T = "0123456789ABCDEF"
        q, r = divmod(n,base)
        if q ==0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    
    # 소수판별
    def isPrime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    num = convert(n,k)
    num_list = num.split('0')

    for x in num_list:
        if x and x!='1' and isPrime(int(x)):
            answer +=1
    
    return answer