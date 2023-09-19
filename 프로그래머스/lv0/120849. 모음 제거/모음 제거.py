def solution(my_string):
    vowel={'a':'a','e':'e','u':'u','o':'o','i':'i'}
    answer = ''
    for string in my_string:
        if string not in vowel.keys():
            answer+=string
    return answer