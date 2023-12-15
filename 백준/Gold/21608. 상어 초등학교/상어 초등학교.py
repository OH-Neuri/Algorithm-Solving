import sys

n = int(sys.stdin.readline())

seat = [[0]*(n+1) for _ in range(n+1)]
input_info = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n**2):

    # 입력 정보 저장
    info = list(map(int, sys.stdin.readline().split()))

    # 현재 학생의 번호
    now_student = int(info[0])

    # 현재 학생이 좋아하는 학생의 번호
    like_student = list(map(int, info[1:]))

    # 학생의 번호 별 좋아하는 학생의 번호를 별도로 저장
    input_info.append(info)

    # 현재 학생을 앉힐 수 있는 자리 후보군
    result = []

    for i in range(1, n+1):
        for j in range(1, n+1):

            # 해당 좌석이 빈 좌석일 경우에만
            if (seat[i][j] == 0):
                # 인접한 칸의 좋아하는 학생의 수
                like_student_count = 0
                # 인접한 칸의 비어있는 칸 수
                empty_count = 0

                # 각 위치에서 상하좌우 탐색
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (1 <= nx < n+1 and 1 <= ny < n+1):    

                        # 인접한 칸에 좋아하는 학생이 있다면, 카운트
                        if (seat[nx][ny] in like_student):
                            like_student_count += 1

                        # 인접한 칸이 비어있다면, 카운트
                        if (seat[nx][ny] == 0):
                            empty_count += 1

                # 현재의 중심 좌석을 현재 학생을 앉힐 수 있는 자리 후보군에 추가
                result.append((like_student_count, empty_count, i, j))

    # 자리 후보군을 조건에 따라 정렬
    result = sorted(result, key = lambda x : (-x[0], -x[1], x[2], x[3]))

    # 최적의 자리에 현재 학생 앉히기
    seat[result[0][2]][result[0][3]] = now_student

# 학생의 번호 별 좋아하는 학생의 번호를 저장할 리스트를 학생의 번호를 기준으로 오름차순 정렬
input_info.sort()

# 학생의 만족도 구하기
sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):

        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            # 교실 내에 있는지
            if (1 <= nx < n+1 and 1 <= ny < n+1):
                if (seat[nx][ny] in input_info[seat[i][j]-1]):
                    count += 1

        if (count != 0):
            sum += 10**(count-1)

print(sum)