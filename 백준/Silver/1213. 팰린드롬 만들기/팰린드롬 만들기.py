alcnt = [0] * 30
# A가 65이므로 -65를 할 것 ord() chr()
input = input()
for i in input:
    alcnt[ord(i)-65] += 1
cnt = 0
for i in range(30):
    if alcnt[i] % 2 == 1:
        cnt += 1
        oddindex = i
answer = ""
if cnt == 1:
    alcnt[oddindex] -= 1
    lts = chr(oddindex+65)
    
if cnt > 1:
    print("I'm Sorry Hansoo")
else:    
    for i in range(30):
        answer += (alcnt[i] // 2) * chr(i+65)
    data = answer[::-1]
    if cnt == 1:
        print(answer + lts + data)
    else:
        print(answer + data)