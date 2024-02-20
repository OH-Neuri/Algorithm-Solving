from heapq import heapify,heappop,heappush
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int,input().split())
    graph[s].append((e,v))

S, E = map(int,input().split())

def dijkstra(start,end):
    dist = [float('inf')] * (N+1)
    visited = [False]*(N+1)
    heap = [(0,start)]
    dist[start] = 0

    while heap:
        start_dist, start_node = heappop(heap)
        if visited[start_node]:
            continue
        visited[start_node] = True

        for next_node, next_dist in graph[start_node]:
            distance = start_dist + next_dist
            if distance < dist[next_node]:
                dist[next_node] = distance
                heappush(heap, (distance, next_node))

    return dist[end]

print(dijkstra(S,E))
