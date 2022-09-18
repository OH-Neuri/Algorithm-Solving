import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

hashmap = {}
for i in a:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for i in b:
    if i in hashmap:
        print(hashmap[i], end=" ")
    else:
        print(0, end=" ")
print()