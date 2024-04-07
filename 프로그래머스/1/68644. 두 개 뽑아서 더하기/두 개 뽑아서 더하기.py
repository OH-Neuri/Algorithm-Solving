def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            tmp = numbers[i]+numbers[j]
            if tmp not in answer:
                answer.append(tmp)
    answer.sort()
    return answer