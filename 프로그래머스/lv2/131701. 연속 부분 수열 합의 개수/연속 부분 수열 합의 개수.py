def solution(elements):
    
    answer = []
    elements_list = elements[:] + elements[:]
    arr = []
    for i in range(len(elements)):
        for j in range(len(elements)):
            arr.append(sum(elements_list[j:j+i+1]))
    
    arr = set(arr)
    return len(list(arr))