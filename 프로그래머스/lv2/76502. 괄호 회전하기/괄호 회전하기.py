def solution(s):
    answer = -1
    
    def rotation(s):
        s = list(s)
        word = s.pop(0)
        s.append(word)
        return s
    
    def check(s):
        stack = []
        for x in s:
            if x == '[' or x == '(' or x == '{':
                stack.append(x)
            if x == ']':
                if len(stack) > 0 and stack[-1]=='[':
                    stack.pop()
                else: return 0 
            if x == ')':
                if len(stack) > 0 and stack[-1]=='(':
                    stack.pop()
                else: return 0 
            if x == '}':
                if len(stack) > 0 and stack[-1]=='{':
                    stack.pop()
                else: return 0 
            
        if len(stack)==0:
            return 1
        else:
            return 0
    
    for i in range(len(s)):
        s_rotation = rotation(s)
        answer += check(s_rotation)
        s = s_rotation
    
    return answer + 1
