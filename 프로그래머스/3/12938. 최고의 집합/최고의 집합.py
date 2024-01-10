def solution(n, s):
    if n>s:
        return [-1]
    elif n==s:
        return n
    answer = []
    for i in range(n-(s%n)):
        answer.append(s//n)
    for i in range(s%n):
        answer.append((s//n)+1)
    
    return answer