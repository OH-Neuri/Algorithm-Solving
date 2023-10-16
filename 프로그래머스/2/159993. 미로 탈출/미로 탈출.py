from collections import deque
def solution(maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    r = len(maps[0])
    c = len(maps)
    
    def BFS(i,j,word):
        q = deque()
        q.append((i,j,0))
        while q:
            x, y, cnt = q.popleft()
            if maps[x][y] == word:
                if word == 'L':
                    return (x,y,cnt)
                elif word =='E':
                    return x,y,cnt
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<c and 0<=ny<r:
                    if not visited[nx][ny] and maps[nx][ny]!='X':
                        visited[nx][ny] = True
                        q.append((nx,ny,cnt+1))
        return x,y, False
    
    visited = [[False] * r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            if maps[i][j]=='S':
                x,y,L= BFS(i,j,'L')
                if not L:
                    return -1
                else:
                    visited = [[False] * r for _ in range(c)]
                    x,y,E = BFS(x,y,'E')
                    if not E:
                        return -1
                    else:
                        return E+L
                    
