def solution(wallpaper):
    L, U = 51, 51
    R, D = -1, -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if U == 51 and wallpaper[i][j] =='#':
                U = i
            if L > j and wallpaper[i][j] =='#':
                L=j    
            if R < j and wallpaper[i][j] =='#':
                R=j
            if D < i and wallpaper[i][j] =='#':
                D=i
                
    answer = [U, L, D+1, R+1]
    return answer