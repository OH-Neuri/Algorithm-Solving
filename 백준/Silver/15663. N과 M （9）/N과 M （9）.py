N, M = map(int,input().split())
nums = sorted((list(map(int,input().split()))))
count = {}
for i in nums:
    if i not in count.keys():
        count[i] = 1
    else:
        count[i] += 1

answer = [0] * M
def per(depth):
    if depth==M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in count.keys():
        if count[i] > 0:
            count[i] -=1
            answer[depth] = i
            per(depth+1)
            count[i] +=1

per(0)
