def solution(n, lost, reserve):
    f_lost = [x for x in lost if x not in reserve]
    f_reserve = [x for x in reserve if x not in lost]
    
    f_lost.sort()
    f_reserve.sort()
    
    student = n - len(f_lost)
    for l in f_lost:
        if l in f_reserve:
            student+=1
            f_reserve.remove(l)
        elif l-1 in f_reserve:
            f_reserve.remove(l-1)
            student+=1
            continue
        elif l+1 in f_reserve:
            f_reserve.remove(l+1)
            student+=1
            continue
        
    return student