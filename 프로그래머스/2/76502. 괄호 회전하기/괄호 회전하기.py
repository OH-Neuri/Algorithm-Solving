from collections import deque
def solution(s):
    q = deque()
    q.extend(list(s))
    rotate = 0
    answer = 0
    
    while rotate!=len(s):
        if check(q):
            answer +=1
        q.rotate(-1)
        rotate+=1
    return answer


def check(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if 2 <= len(stack):
            if stack[-2] =='(' and stack[-1] ==')':
                stack.pop()
                stack.pop()
            elif stack[-2] =='[' and stack[-1] ==']':
                stack.pop()
                stack.pop()
            elif stack[-2] =='{' and stack[-1] =='}':
                stack.pop()
                stack.pop()
    
    if len(stack)==0:
        return True
    else:
        return False
    
    