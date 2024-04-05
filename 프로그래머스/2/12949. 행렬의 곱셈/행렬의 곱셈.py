def solution(arr1, arr2):
    
    l_1 = len(arr1)
    l_2 = len(arr2[0])
    answer= [[0 for _ in range(l_2)] for _ in range(l_1)]
    
    for i in range(l_1):
        for j in range(l_2):
            for idx in range(len(arr2)):
                answer[i][j] += (arr1[i][idx] * arr2[idx][j]) 
                
    return answer