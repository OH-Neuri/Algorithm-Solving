import sys
input= sys.stdin.readline

n = int(input())
list = []

for i in range(n):
  s,e = map(int,input().split())
  list.append([s,e])

list.sort(key = lambda x : (x[1],x[0]))

cnt = 0
k = 0 
for i in range(len(list)):
    if k<=list[i][0]:
        k=list[i][1]
        cnt+=1
print(cnt)