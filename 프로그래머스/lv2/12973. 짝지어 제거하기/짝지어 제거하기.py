def solution(s):
    stack = []
    for i in range(len(s)):
        # push: 비어있거나, 위에 있는 글자랑 다를 경우
        # pop : 위에 있는 글자랑 같은 경우
        if len(stack)==0 or stack[len(stack)-1] != s[i]:
            stack.append(s[i])
        else : stack.pop()

    return 1 if len(stack)==0 else 0