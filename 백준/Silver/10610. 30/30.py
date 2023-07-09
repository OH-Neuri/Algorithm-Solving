n = input()
n = sorted(n, reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for x in n:
      sum += int(x)
    if sum % 3!=0:
        print(-1)
    else:
        print(''.join(n))
# 합이 3의 배수가 안되면 어차피 순서 바꿔도 안됨