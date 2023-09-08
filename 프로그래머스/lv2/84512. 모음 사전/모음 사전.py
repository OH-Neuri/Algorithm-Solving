import itertools
def solution(word):
    arr = []
    for i in range(1,6):
        for x in itertools.product(['A','E','I','O','U'],repeat = i):
            arr.append(''.join(x))
    arr.sort()
    answer = arr.index(word)+1
    return answer