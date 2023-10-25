def solution(n):
    triangle = [ [0] * n for _ in range(n) ]
    answer = []
    x, y = -1, 0
    num = 1
    # n=5, [1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14],[15]
    
    for i in range(n):
        for j in range(i, n):
            # Down
            if i % 3 == 0:
                x += 1
            # Right
            elif i % 3 == 1:
                y += 1
            # Up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            triangle[x][y] = num
            num += 1

    for i in range(n):
        for j in range(i+1):
            answer.append(triangle[i][j])

    return answer