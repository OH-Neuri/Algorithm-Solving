import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N+1)
    
    for start,end,cost in road:
        graph[start].append([end,cost])
        graph[end].append([start,cost])
    heap = []
    distance[1] = 0
    heapq.heappush(heap,[0,1])
    
    while heap:
        print(heap )
        curr_cost,curr_node = heapq.heappop(heap)
        print(curr_cost,curr_node)
        for next_node,next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if total_cost < distance[next_node]:
                distance[next_node] = total_cost
                heapq.heappush(heap,(total_cost,next_node))

    for i in distance:
        if i <= K:
            answer += 1
    return answer