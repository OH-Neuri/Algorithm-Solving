import sys
input = sys.stdin.readline

N = int(input())
matrix = []
tmp_x, tmp_y = -1, 0
for _ in range(N):
    y, x = map(int,input().split())
    if tmp_x == x:
        for i in range(tmp_y,y):
            matrix.append(tmp_x)
        tmp_y = y
    else:
        tmp_x = x

l = len(matrix)

K = int(input())
hole = [-1] * l
for i in range(K):
    y1, x1, y2, x2 = map(int,input().split())
    for j in range(y1,y2):
        hole[j] = x1

answer = 0
for i in range(len(matrix)):
    max_left = 1e9
    hole_left = -1
    max_right = 1e9
    hole_right = -1

    if hole[i]!=-1 or matrix[i]==0: # 자리에 구멍이 있으면 패스
        continue

    for j in range(i-1,-1,-1): # 왼쪽
        max_left = min(matrix[j],max_left)
        if hole[j]!=-1:
            hole_left = hole[j]
            break
    for j in range(i+1,l): # 오른쪽
        max_right = min(matrix[j],max_right)
        if hole[j]!=-1:
            hole_right = hole[j]
            break

    if hole_left == -1 and hole_right == -1: # 구멍이 없는 경우
        answer += matrix[i]
    elif hole_left == -1 and hole_right != -1: # 왼쪽에 구멍이 없는 경우
        h = min(max_right,hole_right)
        # print(max_right,hole_right,1232)
        if matrix[i]-h >0:
            answer += matrix[i]-h
    elif hole_right == -1 and hole_left != -1: # 오른쪽에 구멍이 없는 경우
        h = min(max_left, hole_left)
        if matrix[i]-h >0:
            answer += matrix[i]-h
    else:                 # 양쪽에 구멍이 있는 경우
        h1 = min(max_left,hole_left)
        h2 = min(max_right,hole_right)
        h = max(h1,h2)
        if matrix[i] - h > 0:
            answer += matrix[i] - h
print(answer)
