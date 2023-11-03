#유형: 탐색-DFS => N개수 30만개, 간선 백만
#거리가 K인 노드들 출력하기

# 인접 노드들 탐색 인접리스트로 저장
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
from collections import deque
N, M, K, X = map(int,input().split())
node = [[] for _ in range(N+1)]

# 모든 도로 정보 입력 받기
for _ in range(M):
    s, e = map(int,input().split())
    node[s].append(e)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0

# BFS
q = deque([X])
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in node[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now]+1
            q.append(next_node)

check = False
for i in range(1, N+1):
    if distance[i]==K:
        print(i)
        check = True
if check == False:
    print(-1)