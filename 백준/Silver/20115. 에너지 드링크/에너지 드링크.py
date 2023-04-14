import math
import sys
input = sys.stdin.readline
n= int(input())
amount = list(map(int,input().split(" ")))
max=0
sum=0

for i in amount:
    if i>=max:
        max=i
    sum+=i/2
    
result = sum + (max/2)
if result % 1 ==0:
    print(math.floor(result))
else:
    print(result)
