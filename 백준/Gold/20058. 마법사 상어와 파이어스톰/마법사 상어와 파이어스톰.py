from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
N, Q = map(int,input().split())
C = 2**N
ice_sum = 0 # 남아있는 얼음의 합
matrix = [] # 얼음판
for i in range(C):
    data = list(map(int,input().split()))
    ice_sum += sum(data)
    matrix.append(data)
L = list(map(int,input().split())) # 시전한 단계 리스트

melt = deque()
for l in L:
    length = 2**l
    for t1 in range(0,C,length):
        for t2 in range(0,C,length):
            # 얼음판 한칸 저장 배열
            tmp_row = [[] for _ in range(length)]
            for i in range(length):
                for j in range(length):
                    tmp_row[i].append((matrix[i+t1][j+t2]))

            for i in range(length):
                for j in range(length):
                    matrix[j+t1][length-1-i+t2] = tmp_row[i][j]

    # 녹인다
    for i in range(C):
        for j in range(C):
            chk = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 > nx or nx >= C or 0 > ny or ny >= C or matrix[nx][ny] <= 0:
                    chk +=1
            if chk >= 2:
                melt.append((i,j))
    while melt:
        i, j = melt.popleft()
        if matrix[i][j] > 0:
            matrix[i][j] -=1
            ice_sum -=1

# 가장 큰 얼음판 덩어리 찾기
def BFS(i,j):
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    ice = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<C and 0<=ny<C and not visited[nx][ny] and matrix[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx,ny))
                ice += 1
    return ice

visited = [[False] * C for _ in range(C)]
ice_board = 0
for i in range(C):
    for j in range(C):
        if not visited[i][j] and matrix[i][j] > 0:
            ice_board = max(ice_board, BFS(i,j))

print(ice_sum)
print(ice_board)