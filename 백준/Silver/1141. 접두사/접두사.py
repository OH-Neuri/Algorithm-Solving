import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline()).rstrip() for _ in range(n)]

words.sort(key=len)
res = 0

for i in range(n):
    flag = False
    # 현재 단어보다 길이가 긴 단어를 확인
    for j in range(i + 1, n):
        # 현재 단어가 접두사인지 확인
        if words[i] == words[j][0:len(words[i])]:
            flag = True
            break
    
    # 현재 단어가 접두사가 아니라면 res 카운트
    if not flag:
        res += 1

print(res)