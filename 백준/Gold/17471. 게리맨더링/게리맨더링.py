import sys
from collections import deque
INF = sys.maxsize
def combinations(array,cnt):
    result = []
    if cnt ==0:
        return [[]]
    for i in range(len(array)):
        elementary = array[i]
        rest_array = array[i+1:]
        for c in combinations(rest_array,cnt-1):
            result.append([elementary]+c)
    return result
def bfs(v):
    start = v[0]
    que = deque()
    que.append(start)
    visited = [-1]*(n+1)
    visited[start] = 1
    cnt = 1
    total = 0
    while que:
        now = que.popleft()
        total += people[now]
        for next in graph[now]:
            if visited[next] == -1 and next in v:
                que.append(next)
                visited[next] = 1
                cnt += 1
    return total, cnt
if __name__=='__main__':
    n = int(input())
    people = [0]+ list(map(int,input().split()))
    graph = [[]]
    for i in range(1,n+1):
        _, *A = map(int, input().split())
        graph.append(A)
    cities = [i for i in range(1,n+1)]
    answer = INF
    for i in range(1,n//2+1):
        comb = list(combinations(cities,i))
        for c in comb:
            total1, cnt1 = bfs(c)
            total2, cnt2 = bfs([i for i in range(1,n+1) if i not in c])
            if cnt1+cnt2 == n:
                answer = min(answer,abs(total1-total2))
    print(answer if answer != INF else -1)