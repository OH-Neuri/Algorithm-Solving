import math

def solution(n):
    sum=0;
    while(n>0):
        
        sum+=n%10
        n=(n//10)
        print(n)


    return sum