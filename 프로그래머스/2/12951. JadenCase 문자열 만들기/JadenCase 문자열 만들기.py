def solution(s):
    answer = ''
    s = list(s)
    flag = False # 첫문자 확인
    for word in s:
        # 첫문자일 경우
        if not flag:
            flag = True
            if word.islower():
                answer += word.upper()
                continue
        else:
            if word.isupper():
                answer += word.lower()
                continue
        answer += word
        if word == ' ':
            flag = False
        
    return answer
