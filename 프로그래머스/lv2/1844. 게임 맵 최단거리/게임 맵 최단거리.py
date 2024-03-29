from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solution(maps): 
    
    def BFS():
        q = deque()
        q.append((0,0))
        
        while q:
            x, y = q.popleft()
            
            # 도착하면 출력
            if x == len(maps)-1 and y == len(maps[0])-1:
                return (maps[x][y])
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                # 맵 안에 있고
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny]==1:
                        maps[nx][ny] = maps[x][y]+1
                        q.append((nx,ny))
        return -1
    
    return BFS()


        
    