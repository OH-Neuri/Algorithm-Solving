N = int(input())

prime_number = [True]*(N+1)

# 소수 배열, 소수면 False
for i in range(2, N+1):
    if prime_number[i]:
        for j in range(i+i,N+1,i):
            prime_number[j] = False

# 소수 구간합 배열
s = 0
prime_number_sum = []
for i in range(2, len(prime_number)):
    if prime_number[i]:
        s += i
        prime_number_sum.append(s)

answer =0
left, right = -1, 0
# print(prime_number)
# print(prime_number_sum)
while right<len(prime_number_sum) and left<=right:
    if left == -1 :
        s = prime_number_sum[right]
    else:
        s = prime_number_sum[right] - prime_number_sum[left]
    if s > N :
        left += 1
    else:
        right += 1
        if s == N :
            # print(left,right)
            answer += 1
print(answer)
# left, right 투 포인터로 구간합 구하기
