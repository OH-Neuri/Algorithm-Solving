from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    A, B = map(str,input().split(" "))
    prime_number = [0 for _ in range(10000)]

    # 소수 배열
    for i in range(2, 100):
        for j in range(2*i,10000,i):
            prime_number[j]=1

    # 소수 확인 함수
    def isPrime(i):
        return prime_number[i]==0

    def BFS():
        q = deque([int(A)])
        prime_number[int(A)] = 1
        while q:
            curr = q.popleft()
            strNow = str(curr)
            if curr==int(B):
                print(prime_number[int(curr)]-1)
                return
            for i in range(4):
                for j in range(10):
                    temp = int(strNow[:i] + str(j) + strNow[i+1:])
                    if isPrime(temp) and prime_number[temp]==0 and temp>=1000:
                        prime_number[temp] += prime_number[curr]+1
                        q.append(temp)
    BFS()
