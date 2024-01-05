def solution(elements):
    l = len(elements)
    elements *=2
    return  len(set((sum(elements[j:j+n]) for j in range(l) for n in range(1,l+1))))
