def solution(array, n):
    answer = 0
    for x in array:
        if x==n:
            answer +=1
    return answer