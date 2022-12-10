import sys
input = sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
a.sort(key= lambda x: (x[0],x[1]))
for i in range(n):
    print(a[i][0], a[i][1])