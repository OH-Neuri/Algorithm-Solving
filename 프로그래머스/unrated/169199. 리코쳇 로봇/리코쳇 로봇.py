from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    
    answer = 0
    cnt = 0
    visited = []
    for _ in range(len(board)):
        visited.append([0]*len(board[0]))
        
    def BFS(x, y):
        q = deque()
        q.append((x,y))
        visited[y][x]=1
        while q:
            x, y = q.popleft()
            
            if board[y][x]=="G":
                return visited[y][x]-1
            
            # 미끄러지기
            for k in range(4):
                # 처음 값 기억하기
                nx, ny = x, y
                while True:
                    nx = nx + dx[k]
                    ny = ny + dy[k]
                    # 처음 방문하는 장애물일 경우
                    if 0<=nx<len(board[0]) and 0<=ny<len(board) and board[ny][nx]== "D":
                        nx -= dx[k]
                        ny -= dy[k]
                        break
                    # 처음 방문하는 배열 경계일 경우
                    if nx<0 or nx>=len(board[0]) or ny<0 or ny>=len(board):
                        nx -= dx[k]
                        ny -= dy[k]
                        break
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx,ny))
        return -1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                answer = BFS(j,i)
    
    return answer