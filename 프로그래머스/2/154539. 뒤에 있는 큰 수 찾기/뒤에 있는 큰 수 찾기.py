def solution(numbers):
    answer = [-1 for _ in numbers]

    stack = []
    for i in range(len(numbers)-1):
        stack.append(i)
        if numbers[i] < numbers[i+1]:
            while stack and numbers[stack[-1]] < numbers[i+1]:
                answer[stack.pop()] = numbers[i+1]

    return answer