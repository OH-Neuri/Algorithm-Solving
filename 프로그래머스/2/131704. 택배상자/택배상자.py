from collections import deque
def solution(order):
    answer = []
    stack = []
    order = deque(order)
    for i in range(1, len(order)+1):
        stack.append(i)
        while order:
            if stack and stack[-1] == order[0]:
                answer.append(order.popleft())
                stack.pop()
            else:
                break

    return len(answer)
print(solution([1,2,3,4,5]))