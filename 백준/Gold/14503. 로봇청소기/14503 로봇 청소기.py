# 구현 - 시뮬레이션
# 현재칸 - 청소
# 주변 4칸 청소X -> 후진 -> 탐색 or 종료
# 주변 4칸 청소O -> 반시계 회전 -> 앞 청소할 수 있으면 가고 아니면 돌아
# 앞에 청소 가능하면 전진 후 청소
# 앞에 청소 못하면 돌기 -> 4방향 다 청소 못하면 후진 벽만나면 게임오버
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1
                break

    if flag == 0:
        if graph[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]