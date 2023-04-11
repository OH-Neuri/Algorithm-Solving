import sys
N, M = map(int,input().split())
visited = list(map(int,input().split()))
visited.insert(0,0)

# 구간한 저장할 리스트
visitedSum=[0 for _ in range(N + 1)]
# 구간합 구하기 위한 변수 sum1, sum2
sum1=0
sum2=0
for i in range(N+1):
    sum1+=visited[i]
    if i>M-1:
        sum2+=visited[i-M]
        visitedSum[i]=sum1-sum2
max = max(visitedSum)
if max>0:
    print(max)
    print(visitedSum.count(max))
else:
    print("SAD")
#sys.exit()

