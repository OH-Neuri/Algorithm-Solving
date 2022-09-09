import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    str=input()
    i=0
    for j in range(len(str)-1):
        if str[j]=='(':
            i+=1
        else:
            i-=1
        if i<0:
            print("NO")
            break
    if i==0:
        print("YES")
    elif i<0:
        continue
    else:
        print("NO")
