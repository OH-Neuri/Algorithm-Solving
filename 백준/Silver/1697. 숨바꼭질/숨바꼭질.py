from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int,input().split(" "))
visited = [0] * 1000001
# min_time = sys.maxsize
# def BFS(location):
#     global min_time
#     q = deque()
#     q.append([location,0])
#     while q:
#          l, time = q.popleft()/
#          visited[l]=1
#          # 처음 도착한 시간 저장
#          if l == K :
#              min_time = time
#              break
#          # 처음 도착한 시간 보다 더 빠를 경우만 큐에 들어감
#          elif min_time>time:
#              if l+1 <1000001 and visited[l+1]==0  :
#                 q.append([l+1,time+1])
#              if l-1>=0 and visited[l-1]==0 :
#                 q.append([l-1,time+1])
#              if  l*2 <1000001 and visited[l*2]==0 :
#                 q.append([l * 2, time + 1])
# BFS(N)
# print(min_time)


# 1. 들어가자마자 방문처리
# 2. 큐에 들어가면서 연산 x -> 연산 하고 넣기
# 3. 배열에 값이 있으면 방문 한 것.
def OOB(i):
    return 0<=i<=100000

def BFS():
    q = deque([N])
    # visited[N] = 1
    while q:
         l =q.popleft()
         # 처음 도착한 시간 저장
         if l == K :
             print(visited[l])
             break
         # N값이 범위에 들고, 방문을 안했으면 큐에 (값과 방문 횟수)를 넣어라
         # N값이 범위에 들고, 방문을 안했으면 배열에 방문 횟수를 넣어라.
         for i in (l-1,l+1,l*2):
             if OOB(i) and not visited[i]:
                 visited[i] += visited[l]+1
                 q.append(i)
BFS()
