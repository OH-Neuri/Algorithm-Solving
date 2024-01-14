import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
dx = [0,-1,0]
dy = [-1,0,1]

N, M, D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

a_list = list(combinations([i for i in range(M)], 3))

# 궁수 위치 배정
def game(a):
    tmp = copy.deepcopy(arr)
    answer = 0
    #  궁수 위치
    for i in range(N-1,-1,-1):
        this_turn = []
        for ay in a:
            q = deque([(i,ay,1)])
            while q:
                x, y, d = q.popleft()
                if tmp[x][y] == 1:
                    this_turn.append((x,y))
                    break

                if d < D:
                    for k in range(3):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0<=nx<N and 0<=ny<M:
                            q.append((nx,ny,d+1))

        for x, y in this_turn:
            if tmp[x][y] == 1:
                tmp[x][y] = 0
                answer +=1

    return answer
# 적 공격
result = 0
for i in a_list:
    result = max(game(i),result)
print(result)