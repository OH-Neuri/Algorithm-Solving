def solution(numbers):
    l = len(numbers)
    answer = [-1 for _ in range(l)]
    stack = []
    
    for i in range(l):
        while stack and  numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer