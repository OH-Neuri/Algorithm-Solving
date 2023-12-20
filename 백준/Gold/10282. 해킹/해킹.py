import heapq
import sys
input = sys.stdin.readline

# 감염된 컴퓨터 => visited True 개수
# 가중치 갱신

tc = int(input())
for _ in range(tc):

    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    dist = [float('inf') for _ in range(n+1)]

    for _ in range(d):
        s, e, v = map(int,input().split())
        graph[e].append((s,v))

    def dijkstra(start):  # start로 부터의 거리 값을 저장하기 위함
        q = []
        dist[c] = 0  # 시작 값은 0
        heapq.heappush(q, [dist[start],start])

        while q:
            curr_dist, curr_dest = heapq.heappop(q)

            if dist[curr_dest] < curr_dist: # 기존에 있는 거리보다 길다면, 볼 필요 없음
                continue

            for new_dest, new_dist in graph[curr_dest]:
                distance = curr_dist + new_dist # 해당 노드를 거쳐 갈 때 거리
                if distance < dist[new_dest]: # 알고 있는 거리보다 작으면 갱신
                    dist[new_dest] = distance
                    heapq.heappush(q, [distance, new_dest]) # 다음 인접 거리를 계산하기 위해 큐에 삽입

    dijkstra(c)

    com_cnt = 0
    com_time = 0
    for i in dist:
        if i != float('inf'):
            com_time = max(com_time,i)
            com_cnt +=1
    print(com_cnt, com_time)