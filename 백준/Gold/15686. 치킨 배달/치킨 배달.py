from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]


N, M = map(int,input().split())
city = [] # 도시
chicken = [] # 치킨집 좌표
home = [] # 집 좌표
for i in range(N):
    data = list(map(int,input().split()))
    city.append(data)
    for j in range(N):
        if data[j] == 2:
            chicken.append((i,j))
        if data[j] == 1:
            home.append((i,j))

l_ch = len(chicken)
min_value = 1e9

# 조합으로 뽑은 치킨집 좌표
for chickens in (list(combinations([x for x in range(l_ch)],M))):
    value = 0
    for x, y in home:
        dist = 1e9
        for i in chickens:
            dist = min(dist,abs(x-chicken[i][0])+abs(y-chicken[i][1]))
        value += dist
    min_value = min(min_value, value)
print(min_value)
