
import sys
input = sys.stdin.readline

# N: 노드 개수, M: 간선 개수
N, M = map(int,input().split())

edges = []
dist = [float('inf')] * (N+1)
dist[1] = 0
for _ in range(M):
    a, b, w = map(int,input().split())
    edges.append((a,b,w))

isCycle = False
for i in range(N):
    for start, end, w in edges:
        # 방문했던 노드일 경우
        if dist[start] != float('inf'):
            distance = dist[start] + w
            if distance < dist[end]:
                # N번째 반복 때 거리가 업데이트 됐다면,
                if i == N-1 :
                    isCycle= True
                dist[end] = distance

if isCycle:
    print(-1)
else:
    for i in dist[2:]:
        # 갈 수가 없음
        if i == float('inf'):
            print(-1)
        else:
            print(i)
