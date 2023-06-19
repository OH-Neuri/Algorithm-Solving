n = int(input())

d = [[1 for i in range(10)]]
for i in range(n):
    d.append([0 for j in range(10)])

for i in range(1,n+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]
print(d[n][9]%10007)
