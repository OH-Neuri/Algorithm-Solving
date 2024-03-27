from collections import deque
from heapq import heappush, heappop
def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    for s, e, d in road:
        graph[s].append([e,d])
        graph[e].append([s,d])
        
    dist = [float('inf')] * (N+1)
    heap = [(0,1)]
    dist[1] = 0
    visited = [False] * (N+1)
    answer = 0
    
    while heap:
        start_dist, start_node = heappop(heap)
        if visited[start_node] :
            continue
        visited[start_node] = True
        
        for next_node, next_dist in graph[start_node]:
            distance = start_dist + next_dist
            if dist[next_node] > distance:
                dist[next_node] = distance
                heappush(heap, (distance,next_node))
                
    for d in dist:
        if d<=K:
            answer+=1
    return answer
            