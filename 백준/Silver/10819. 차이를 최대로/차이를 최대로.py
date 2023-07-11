import sys, itertools
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split(" ")))
nPr = list(itertools.permutations(arr,N))
max_sum=0
for i in range(len(nPr)):
    sum=0
    for j in range(N-1):
        sum += abs(nPr[i][j]-nPr[i][j+1])
    if sum>max_sum:
        max_sum = sum
print(max_sum)