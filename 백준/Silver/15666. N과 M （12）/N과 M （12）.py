N, M = map(int,input().split())
nums = list(map(int,input().split()))
answer = [0] * M
count = {}

for num in nums:
    if num not in count.keys():
        count[num] = 1
    else: count[num] +=1

count_value = sorted(count.items())

def com(depth, idx):
    if depth == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(idx, len(count_value)):
        answer[depth] = count_value[i][0]
        com(depth+1,i)

com(0,0)