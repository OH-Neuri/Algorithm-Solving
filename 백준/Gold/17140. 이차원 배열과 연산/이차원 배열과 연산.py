import sys

r, c, k = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def calculate(matrix, dir): # 배열A의 연산
    new_matrix, length = [], 0 # 연산 후 반환할 행렬 / 최대 길이의 행(또는 열)
    for row in matrix:
        num_cnt, new_row = [], [] # (숫자, 개수)를 담을 배열 / 연산 후의 행(또는 열)을 담을 배열
        for num in set(row): # 각 숫자에 대해서 개수를 파악 
            if num == 0: continue # 0일 경우 continue
            cnt = row.count(num)
            num_cnt.append((num, cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1], x[0]]) # 정렬
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_matrix.append(new_row)
        length = max(length, len(new_row))

    for row in new_matrix: # 가장 긴 행(또는 열)의 크기에 맞춰 0 추가
        row += [0] * (length - len(row))
        if len(row) > 100: row = row[:100] # 크기가 100이 넘어가면 슬라이싱

    return list(zip(*new_matrix)) if dir == 'C' else new_matrix

time = 0
while True:
    if time > 100: time = -1; break # 시간이 100이 넘으면 break
    if 0 <= r-1 < len(matrix) and 0 <= c-1 < len(matrix[0]) and matrix[r-1][c-1] == k: break # (r, c)의 값이 k와 일치하면 break
    if len(matrix) >= len(matrix[0]): # 행의 개수 >= 열의 개수
        matrix = calculate(matrix, 'R')
    else:
        matrix = calculate(list(zip(*matrix)), 'C')
    time += 1
print(time)