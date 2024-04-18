def solution(park, routes):
    x, y = 0, 0
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == 'S':  
                x, y = row, col
    
    op = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    for i in routes:
        dx, dy = op[i.split()[0]] 
        n = int(i.split()[1])  
        
        xx, yy = x, y 
        canmove = True 

        for _ in range(n):
            nx = xx + dx  
            ny = yy + dy 
            

            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                canmove = True
                xx, yy = nx, ny
            else:  # 공원을 벗어낫거나, 장애물이면 이동 불가(False)
                canmove = False
                break
                
        if canmove:  # 이동이 가능하면 위치 반영해주기
            x, y = nx, ny  
        
    return [x, y]