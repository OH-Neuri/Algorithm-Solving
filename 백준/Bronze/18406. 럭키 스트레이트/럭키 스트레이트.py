import sys
input = sys.stdin.readline

N = (input())
L, R  = 0, 0
for i in N[:len(N)//2]:
    L += int(i)
for i in N[len(N)//2:-1]:
    R += int(i)

if L==R:
    print("LUCKY")
else:
    print("READY")