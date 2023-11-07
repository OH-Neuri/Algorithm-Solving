N, M = map(int,input().split())
#4 2

answer = [0] * M
def per(depth):
    if depth == M:
        for i in answer:
            print(i ,end=' ')
        print()
        return

    for i in range(N):
        answer[depth] = i+1
        per(depth+1)
per(0)
