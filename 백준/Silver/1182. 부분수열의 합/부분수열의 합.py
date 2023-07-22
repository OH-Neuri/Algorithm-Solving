from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int,input().split())
nums = list(map(int,input().split()))
answer = 0

for i in range(1,N+1):
    comb = list(combinations(nums,i))
    for x in comb:
        if sum(x)==S:
            answer +=1
print(answer)
