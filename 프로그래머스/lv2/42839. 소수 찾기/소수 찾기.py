from itertools import permutations
def solution(numbers):
    # 1. numbers로 만들 수 있는 숫자 경우의 수
    # 2. set하거나 배열에 저장
    # 3. 소수 판별
    answer = []
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    for i in range(1, len(numbers)+1):
        nums = list(map(''.join, permutations(list(numbers),i)))
        for j in list(set(nums)):
            if isPrime(int(j)):
                answer.append(int(j))
    
    return len(set(answer))