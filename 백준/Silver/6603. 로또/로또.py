from itertools import permutations
import sys
input = sys.stdin.readline

def DFS(depth, idx):

    if depth == 6:
        # print(lotto)
        for x in lotto:
            print(x , end=' ')
        print()
        return

    for i in range(idx, k):
        lotto.append(s[i])
        DFS(depth+1, i+1)
        lotto.pop()

while True:
    nums = list(map(int,input().split()))
    k = nums[0]
    s = nums[1:]
    lotto = []
    DFS(0,0)
    if k == 0:
        exit()
    print()