import sys
input = sys.stdin.readline

N = int(input())
student = list(map(int,input().split()))
B, C = map(int,input().split())

answer = 0
for s in student:
    # answer += (s-B)//C+1 if (s-B)%C==0 else (s-B)//C+2 if (s-B)>0 else 1
    answer +=   1 if (s-B)<=0 else (s-B)//C+1 if (s-B)%C==0 else (s-B)//C+2
print(answer)
