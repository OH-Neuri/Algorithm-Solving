import sys
input = sys.stdin.readline

N, C = map(int,input().split())
house = [int(input()) for _ in range(N)]
house.sort()
start, end = 1, house[N-1] - house[0] #최소거리, 최대거리

result = 0

while start <= end:
    mid = (start+end)//2
    # 거리가 mid 일때 조건에 맞는지 확인
    current = house[0]
    c = 1
    for x in house:
        if x >= current+mid:
            c+=1
            current = x
    if c>=C:
        result = mid
        start = mid +1
    else:
        end = mid-1
print(result)
