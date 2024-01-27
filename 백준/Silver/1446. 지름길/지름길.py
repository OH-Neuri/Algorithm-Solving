import sys
input = sys.stdin.readline
N, D = map(int, input().split())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key = lambda x : (x[0], x[1], x[2]))
distance = [i for i in range(D + 1)]

for i in lst:
    s, e, d = i

    if e <= D:
        distance[e] = min(distance[s] + d, distance[e])

    for j in range(s, D + 1):
        distance[j] = min(distance[j - 1] + 1, distance[j])

print(distance[D])    