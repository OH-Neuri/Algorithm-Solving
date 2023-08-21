def solution(str1, str2):
    answer = ''
    for a, b in zip(str1, str2):
        answer = answer + a + b
    return answer