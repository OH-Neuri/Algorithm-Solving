from collections import deque
import sys

input = sys.stdin.readline


# 종수 이동
def j_move(d):
    d -= 1
    global l_x, l_y
    nx, ny = l_x + dir[d][0], l_y + dir[d][1]
    if matrix[nx][ny] == 'R':  # 이동자리에 미친 아두이노가 있는 경우
        return False
    elif matrix[nx][ny] == 'I':
        return True
    else:  # 이동자리가 미친 아두이노가 없는 경우
        matrix[nx][ny] = 'I'
        matrix[l_x][l_y] = '.'
        l_x, l_y = nx, ny
        return True


# 미아 이동
def m_move(l_x, l_y):
    m_q = deque()
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'R':
                matrix[i][j] = '.'
                # 거리가 가장 작아지는 방향 찾기
                min_dir = -1
                min_dist = 1e9
                for k in range(9):
                    if k == 4:
                        continue
                    tx, ty = i + dir[k][0], j + dir[k][1]
                    if 0 <= tx < R and 0 <= ty < C:
                        dist = abs(l_x - tx) + abs(l_y - ty)
                        if dist < min_dist:
                            min_dist = dist
                            min_dir = k
                nx, ny = i + dir[min_dir][0], j + dir[min_dir][1]
                if nx == l_x and ny == l_y:
                    return False
                m_q.append((nx, ny))

    # -1 : 빈 칸, 0: 한 개 존재, 1 : 폭발
    visited = [[-1] * C for _ in range(R)]
    # 미친 아두이노 이동 위치 검사
    while m_q:
        x, y = m_q.popleft()
        if visited[x][y] == -1:  # 빈 칸일 경우
            visited[x][y] = 0
            matrix[x][y] = 'R'
        elif visited[x][y] == 0:  # 한 개 존재하는 경우
            visited[x][y] = 1
            matrix[x][y] = '.'

    return True


dir = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]  # 방향
R, C = map(int, input().split())  # 행, 열
matrix = []  # 보드
l_x, l_y = -1, -1  # 종수 아두이노 위치

for i in range(R):
    data = list(map(str, input().rstrip()))
    if 'I' in data:  # 종수 위치 저장
        l_x, l_y = i, data.index('I')
    matrix.append(data)

J_list = list(map(int, input().rstrip()))  # 종수 이동방향 리스트
for i in range(len(J_list)):
    if not j_move(J_list[i]):  # 종수 이동
        print("kraj %d" % (i + 1))
        exit()
    if not m_move(l_x, l_y):  # 미친 아두이노 이동
        print("kraj %d" % (i + 1))
        exit()

for m in matrix:
    print("".join(m))
