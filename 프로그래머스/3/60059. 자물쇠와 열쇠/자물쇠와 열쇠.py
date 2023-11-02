# d => 1:90도, 2:180도, 3:270도
def rotate(array,d):
    n = len(array)
    result = [[0] * n for _ in range(n)]

    if d % 4 == 1:
        for r in range(n):
            for c in range(n):
                result[c][n - r - 1] = array[r][c]
    elif d % 4 == 2:
        for r in range(n):
            for c in range(n):
                result[n - r - 1][n - c - 1] = array[r][c]
    elif d % 4 == 3:
        for r in range(n):
            for c in range(n):
                result[n - c - 1][r] = array[r][c]
    else:
        for r in range(n):
            for c in range(n):
                result[r][c] = array[r][c]
    return result
    
# 자물쇠가 모두 1인지 확인
def check(array):
    n = len(array) // 3
    for i in range(n , n*2):
        for j in range(n, n*2):
            if array[i][j] !=1:
                return False
    return True
    
def solution(key, lock):
    n = len(key)
    m = len(lock)
    lock_list = [[0 for _ in range(m*3)] for _ in range(m*3)]
    
    
    # lock 확장하기
    for i in range(m):
        for j in range(m):
            lock_list[i+m][j+m] = lock[i][j]
    
    # 탐색하기
    for i in range(1, m*2):
        for j in range(1, m*2):
            # key 0도, 90도, 180도, 270도 회전하기
            for d in range(4):
                r_key = rotate(key,d)
                for x in range(n):
                    for y in range(n):
                        lock_list[i+x][j+y] += r_key[x][y]
                
                if check(lock_list):
                    return True
                
                for x in range(n):
                    for y in range(n):
                        lock_list[i+x][j+y] -= r_key[x][y]
        
    
    return False