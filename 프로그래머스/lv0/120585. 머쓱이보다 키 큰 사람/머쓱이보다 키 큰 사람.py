def solution(array, height):
    answer = 0
    for x in array:
        if x > height:
            answer+=1
    return answer