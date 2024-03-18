import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(n)]

sum_ = [[0 for _ in range(m+1)] for _ in range(n+1)]

# 누적합 구하기
for i in range(n):
    for j in range(m):
        sum_[i+1][j+1] = sum_[i][j+1] + sum_[i+1][j] - sum_[i][j] + picture[i][j]

# 요구사항 출력하기
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    
    # 평균을 구하기 위한 영역 구하기
    area = (r2 - r1 + 1) * (c2 - c1 + 1)
    
    # 누적합으로 구역합 구해서 영역을 나누기
    print((sum_[r2][c2] - sum_[r2][c1-1] - sum_[r1-1][c2] + sum_[r1-1][c1-1])//area)