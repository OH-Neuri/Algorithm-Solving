from collections import deque

def f_bfs():
    while f_deq:
        x,y = f_deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph 벗어난 좌표는 무시
            if nx < 0 or nx > (r-1) or ny < 0 or ny > (c-1): 
                continue
            '''
            'J'에 해당하는 좌표는 0으로 미리 바꿔뒀기 때문에
            graph[nx][ny] == '.'일 때만 불이 이동할 수 있도록 함.
            '''
            if graph[nx][ny] == '.':
                graph[nx][ny] = graph[x][y] + 1
                f_deq.append([nx,ny])

def j_bfs():
    while j_deq:
        x,y = j_deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # graph를 벗어나면 탈출했음을 의미한다.
            if nx < 0 or nx > (r-1) or ny < 0 or ny > (c-1):
                time = graph[x][y] + 1
                return print(time)  # 탈출!
             #불이 번지지 않았으면 해당 좌표값이 '.'인 경우도 있음을 고려
            if graph[nx][ny] == '.':
                graph[nx][ny] = graph[x][y] + 1
                j_deq.append([nx,ny])
            # 해당 좌표값이 '#'이면 밑의 if문이 오류가 나서 걸러주기 위해 추가
            elif graph[nx][ny] != '#':
                if graph[nx][ny] > (graph[x][y] + 1): # 불의 값이 지훈이보다 크면
                    graph[nx][ny] = graph[x][y] + 1
                    j_deq.append([nx,ny])
    time = 'IMPOSSIBLE' # 지훈이가 탈출하지 못하면 이 문장에 도달   
    return print(time)

# r: 행(x), c: 열(y)
r,c = map(int,input().split())

# graph
graph = []
for i in range(r):
    graph.append(list(input()))

#deque
j_deq = deque()
f_deq = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 지훈, 불 처음 위치 큐에 넣기
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            f_deq.append([i,j])
            graph[i][j] = 0 # 0부터 시작해서 해당 위치 시간 파악
        if graph[i][j] == 'J':
            j_deq.append([i,j])
            graph[i][j]= 0  # 0부터 시작해서 해당 위치 시간 파악

f_bfs() # 불 먼저 bfs돌려서 언제 어디까지 퍼지는지 graph에 표기
j_bfs()