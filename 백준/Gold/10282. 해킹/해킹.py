from heapq import heappush, heappop
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):

    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    dist = [float('inf')]*(n+1)
    visited = [False]*(n+1)
    for _ in range(d):
        s, e, v = map(int,input().split())
        graph[e].append((s,v))


    heap= [(0,c)]
    dist[c] = 0  # 시작 값은 0
    while heap:
        start_dist, start_node = heappop(heap)
        if visited[start_node]:
            continue
        visited[start_node] = True
        time = start_dist

        for next_node, next_dist in graph[start_node]:
            if start_dist + next_dist < dist[next_node]:
                dist[next_node] = start_dist + next_dist
                heappush(heap, (start_dist+next_dist, next_node))

    print(sum(visited), time)
