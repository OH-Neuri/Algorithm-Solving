import sys
input = sys.stdin.readline

N=int(input())
num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

for i in range(N):
    cnt = 1
    for j in range(N):
        if num[i][0]<num[j][0]:
            if num[i][1]<num[j][1]:
                cnt+=1
    print(cnt, end=' ')