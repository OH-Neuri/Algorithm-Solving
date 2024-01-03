def solution(s):
    stack = []
    for i in s:
    # 들어가기
        stack.append(i)
    # 나오기
        if len(stack) >= 2 and stack[-2] == '(' and i == ')':
            stack.pop()
            stack.pop()

    return False if len(stack) else True