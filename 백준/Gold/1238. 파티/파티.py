from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra(start, graph):
    dist = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)
    heap = [(0, start)]
    dist[start] = 0  # 시작
    link_cnt = 0
    while heap:
        start_dist, start_node = heappop(heap)
        if visited[start_node]:
            continue
        visited[start_node] = True

        for next_node, next_dist in graph[start_node]:
            if start_dist + next_dist < dist[next_node]:
                dist[next_node] = start_dist + next_dist
                heappush(heap, (start_dist + next_dist, next_node))
    return dist


N, M, X = map(int, input().split())
go_graph = [[] for _ in range(N + 1)]
back_graph = [[] for _ in range(N + 1)]

link_node_cnt = 0

for _ in range(M):
    s, e, v = map(int, input().split())
    go_graph[e].append((s, v))
    back_graph[s].append((e, v))

go_dist = dijkstra(X, go_graph)
back_dist = dijkstra(X, back_graph)

max_dist = 0
for i in range(1,N+1):
    max_dist = max(go_dist[i]+back_dist[i], max_dist)
print(max_dist)

