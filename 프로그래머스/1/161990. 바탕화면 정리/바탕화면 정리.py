def solution(wallpaper):
    L = 1e9
    U = 1e9
    R = 0
    D = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if U>i and wallpaper[i][j] =='#':
                U = i
            if L > j and wallpaper[i][j] =='#':
                L=j    
            if R<j and wallpaper[i][j] =='#':
                R=j
            if D<i and wallpaper[i][j] =='#':
                D=i
                
    answer = [U,L,D+1,R+1]
    return answer