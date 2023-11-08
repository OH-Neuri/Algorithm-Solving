N, M = map(int,input().split())
nums = list(map(int,input().split()))
count = {}
answer = [0] * M

for num in nums:
    if num not in count.keys():
        count[num] = 1
    else:
        count[num] +=1

count_value= list(sorted(count.items()))

def per(depth):
    if depth == M:
        for i in answer:
            print(i, end =' ')
        print()
        return

    for i in range(len(count_value)):
        if count_value[i][1] > 0:
            answer[depth] = count_value[i][0]
            per(depth+1)

per(0)