from collections import deque
input = __import__('sys').stdin.readline

#소수판별함수
def isPrime(number):
    if number == 1:
        return False
    for i in range(2, int(number**1/2)+1):
        if number % i == 0:
            return False
    return True

#BFS
def bfs(A, B):
    q = deque()
    q.append((A,0))
    while q:
        password, count = q.popleft()
        if password == B:
            print(count)
            return
        for i in range(4):
            for j in range(10):
                new_pass = list(str(password))
                new_pass[i] = str(j)
                new_pass = int(''.join(new_pass))
                if 1000<=new_pass and not visited[new_pass] and prime[new_pass]:
                    visited[new_pass] = 1
                    q.append((new_pass, count+1))
                


#소수판별테이블
prime = [False]
for i in range(1,10000):
    prime.append(isPrime(i))

#테스트케이스
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0]*10000
    visited[A] = 1
    bfs(A,B)