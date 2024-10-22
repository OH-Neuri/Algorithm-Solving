N, X = map(int,input().split())
arr = sorted(list(map(int,input().split())))
s = 0
e = N-1
remain = 0
cnt = 0
while s <= e : # s와 e가 교차되면 멈춘다!

    if arr[e] == X:
        cnt += 1
        e -= 1
        continue

    if s == e :
        remain += 1 
        break
        # 짜투리를 하나 추가한다!

    if arr[e] + arr[s] >= X/2:
        cnt +=1
        s += 1
        e -= 1

    else:
        s += 1 # 수가 커지겠죠!
        remain += 1

print(cnt + remain//3 )