from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int,input().split(" "))
visited = [0] * 1000001
min_time = sys.maxsize
def BFS(location):
    global min_time
    q = deque()
    q.append([location,0])
    while q:
         l, time = q.popleft()
         visited[l]=1
         # 처음 도착한 시간 저장
         if l == K :
             min_time = time
             return
         # 처음 도착한 시간 보다 더 빠를 경우만 큐에 들어감
         elif min_time>time:
             if l+1 <1000001 and visited[l+1]==0  :
                q.append([l+1,time+1])
             if l-1>=0 and visited[l-1]==0 :
                q.append([l-1,time+1])
             if  l*2 <1000001 and visited[l*2]==0 :
                q.append([l * 2, time + 1])
BFS(N)
print(min_time)



