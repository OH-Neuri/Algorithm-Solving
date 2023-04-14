import sys
input = sys.stdin.readline

n= int(input())
file ={}

for i in range(n):
    extension = input().rstrip().split(".")[1]
    if extension in file.keys():
        file[extension] += 1
    else:
        file[extension] = 1

keys = sorted(file.keys())
for i in keys:
    print(i, end=' ')
    print(file[i])
