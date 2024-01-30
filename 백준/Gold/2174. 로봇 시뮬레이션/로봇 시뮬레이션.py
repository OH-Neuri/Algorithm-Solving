import sys
from collections import defaultdict
 
input_func = sys.stdin.readline
if __name__ == '__main__':
    A, B = map(int, input_func().split())
    N, M = map(int, input_func().split())
 
    robots = defaultdict(tuple)
    #문자로 입력받은 방향을 숫자로 변경시켜주기 위한 방향 맵핑 딕셔너리
    directions = {'N': 0, 'W': 1, 'E': 3, 'S': 2}
    for idx in range(N):
        x, y, d = map(str, input_func().split())
        #행 좌표(행 길이-입력행번호), 열 좌표(입력 열번호 - 1)
        robots[idx + 1] = (B - int(y), int(x) - 1, directions[d])
 
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    flag = False
    #명령을 입력받아 수행
    for idx in range(M):
        id, cmd, num = map(str, input_func().split())
        #문자열로 입력받았으니 숫자로 변경
        id, num = int(id), int(num)
        robot_x, robot_y, robot_d = robots.pop(id)
 
        #명령 수행
        if cmd == 'L':
            #4번 회전하면 같은 방향
            num %= 4
            #방향은 4방향
            robot_d = (robot_d + (1 * num)) % 4
        elif cmd == 'R':
            # 4번 회전하면 같은 방향
            num %= 4
            #방향은 4방향
            robot_d = (robot_d + (3 * num)) % 4
        elif cmd == 'F':
            #반복 횟수만큼 한 칸씩 전진
            for n in range(num):
                robot_x += dx[robot_d]
                robot_y += dy[robot_d]
 
                #범위 확인
                if not 0 <= robot_x < B or not 0 <= robot_y < A:
                    print('Robot {} crashes into the wall'.format(id))
                    flag = True
                    break
 
                #동일 위치 로봇 확인, 로봇 딕셔너리 값을 하나씩 비교
                for key, value in robots.items():
                    compare_x, compare_y, _ = value
                    if robot_x == compare_x and robot_y == compare_y:
                        print('Robot {} crashes into robot {}'.format(id, key))
                        flag = True
                        break
                #전진 반복문 종료
                if flag:
                    break
 
        #명령 수행 반복문 종료
        if flag:
            break
 
        #오류 발생하지 않으면, 로봇 딕셔너리에 현재 이동한 로봇 정보 업데이트하여 저장
        robots[id] = (robot_x, robot_y, robot_d)
 
    #정상 종료(오류 발생 X)시 출력
    if not flag:
        print('OK')
