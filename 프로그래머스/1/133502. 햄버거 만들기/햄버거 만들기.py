def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack)>=4 and stack[-4:]==[1,2,3,1]:
            del stack[-4:]
            answer +=1
            
    return answer