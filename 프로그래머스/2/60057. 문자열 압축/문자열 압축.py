def solution(s):
    candi = [i for i in range(1, (len(s)//2+1))]
    answer = len(s)
    
    for length in candi:
        key = s[:length]
        shorten = []
        cnt = 1
        for  i in range(length, len(s), length):
            if key == s[i:i+length]:
                cnt += 1
            else:
                shorten.append([key, cnt])
                cnt = 1
                key = s[i:i+length]
        shorten.append([key, cnt])
        answer = min(answer, sum([len(key) + (len(str(cnt)) if cnt > 1 else 0) for key, cnt in shorten]))
    return answer