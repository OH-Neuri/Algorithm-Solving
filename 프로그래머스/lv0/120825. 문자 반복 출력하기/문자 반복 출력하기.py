def solution(my_string, n):
    answer = ''
    for word in my_string:
        for i in range(n):
            answer+=word
    return answer