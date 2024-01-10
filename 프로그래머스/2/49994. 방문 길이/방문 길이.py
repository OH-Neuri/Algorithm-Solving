def solution(dirs):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    answer = 0
    visited = []
    x, y = 5, 5
    
    for d in dirs:
        if d == 'L':
            nx, ny = x + dx[2], y + dy[2]
        if d == 'U':
            nx, ny = x + dx[3], y + dy[3]
        if d == 'R':
            nx, ny = x + dx[0], y + dy[0]
        if d == 'D':
            nx, ny = x + dx[1], y + dy[1]
        
        if 0<=nx<11 and 0<=ny<11:
            if [x,y,nx,ny] not in visited and [nx,ny,x,y] not in visited:
                answer+=1
                visited.append([x,y,nx,ny])
            x, y = nx, ny    
        
    return answer