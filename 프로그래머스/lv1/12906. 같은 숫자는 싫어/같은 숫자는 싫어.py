def solution(arr):
    stack = [arr[0]]
    idx=0
    for i in range(len(arr)):
        if stack[idx]!=arr[i]:
            idx+=1
            stack.append(arr[i])
    return stack
