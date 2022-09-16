from collections import deque

n,k=map(int,input().split())
que=deque([(i+1) for i in range(n)])

print('<', end='')
while len(que)>1:
    for i in range(k-1):
        que.rotate(-1)
    print(que.popleft(),end=', ')

print(que.popleft(),end='>')