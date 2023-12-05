from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+2)]
    node = [list(map(int,input().split())) for _ in range(n+2)]

    # 거리가 1000이내인 노드들 연결하기
    for s in range(n+2):
        for e in range(s+1,n+2):
            dist = abs(node[s][0]-node[e][0]) + abs(node[s][1]-node[e][1])
            if dist<=1000:
                graph[s].append(e)
                graph[e].append(s)

    # 그래프 탐색
    def BFS(node):
        q = deque()
        q.append(node)
        visited[node] = True
        while q:
            curr = q.popleft()
            #목적지에 도달한 경우
            if curr == (n+1):
                return True

            for next in graph[curr]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        return False

    # BFS로 목적지까지 도달할 수 있는지 확인
    visited = [False]*(n+2)
    if BFS(0):
        print('happy')
    else:
        print('sad')

