N = input()
color = list(input())
check = color[0]
cnt=1
for i in range(1, len(color)):
    if color[i]!=check and color[i]!=color[i-1]:
        cnt+=1;
print(cnt)