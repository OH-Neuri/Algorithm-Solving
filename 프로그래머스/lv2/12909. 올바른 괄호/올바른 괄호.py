def solution(s):
    answer = True
    stack = []
    
    for x in s:
        if x == "(":
            stack.append(s)
        else:
            if len(stack)==0:
                print(0)
                answer = False
                continue
            else:
                stack.pop()
    if len(stack)!=0:
        answer = False
    return answer