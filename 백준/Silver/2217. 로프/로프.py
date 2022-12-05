import sys
input = sys.stdin.readline

N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
num.sort()
for i in range(N):
    num[i]=num[i]*(N-i)
print(max(num))