import sys
input = sys.stdin.readline

x, y, X, Y = map(int,input().split())
num=[x, y, (X-x), (Y-y)]
print(min(num))
