from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
            time_max[i] = times[i-1]
    while q:
        node = q.popleft()
        if node == goal:
            return time_max[node]
        for next in graph[node]:
            indegree[next] -= 1
            time_max[next] = max(time_max[next], time_max[node])
            if indegree[next] == 0:
                time_max[next] += times[next-1]
                q.append(next)
    return times[goal-1]

T = int(input())
for _ in range(T):
    # N: 건물의 개수(노드 수), K: 건설 순서 규칙의 수 (엣지 수)
    N, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]  # 건물 연결 정보
    times = list(map(int, input().split()))  # 건물당 건설에 걸리는 시간
    indegree = [0 for _ in range(N + 1)]
    time_max = [0 for _ in range(N + 1)]
    for _ in range(K):
        s, e = map(int, input().split())
        graph[s].append(e)
        indegree[e] += 1
    goal = int(input())  # 목표 건물

    print(topology_sort())
