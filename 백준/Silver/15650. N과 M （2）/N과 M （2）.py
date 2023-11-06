N, M = map(int,input().split())
# 4 2
answer = [0] * M

def combination(depth, idx):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(idx, N+1):
        answer[depth] = i
        combination(depth+1, i+1)

combination(0,1)