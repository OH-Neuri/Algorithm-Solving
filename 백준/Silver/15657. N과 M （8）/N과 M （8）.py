N, M = map(int,input().split())
nums = sorted(list(map(int,input().split())))

answer = [0] * M
def com(depth,idx):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(idx,N):
        answer[depth] = nums[i]
        com(depth+1,i)
com(0,0)