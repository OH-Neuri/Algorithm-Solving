def solution(sequence, k):
    prefix_sum = [0]
    sum_value = 0
    s = 0
    e = s+1
    result = [0, len(sequence)]
    for i in range(len(sequence)):
        sum_value += sequence[i]
        prefix_sum.append(sum_value)
    
    while s<e and e<len(prefix_sum):
        if prefix_sum[e]-prefix_sum[s] ==k:
            if (e-1)-s < (result[1] - result[0]):
                result = [s,e-1]
            e+=1
        elif prefix_sum[e] - prefix_sum[s] <k:
            e+=1
        else:
            s+=1
    return result