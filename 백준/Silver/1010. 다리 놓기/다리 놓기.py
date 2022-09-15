import sys, math
input = sys.stdin.readline

t =int(input())
for i in range(t):
    x, y = map(int,input().split())
    print(math.comb(y, x))