import sys
input = sys.stdin.readline

n=int(input())
po=[]
for i in range(n):
    x, y = map(int,input().split())
    po.append((x, y))

po.sort(key=lambda x: x[0])
po.sort(key=lambda x: x[1])

for i in po:
    print(i[0], i[1])
