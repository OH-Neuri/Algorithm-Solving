def solution(array):
    array = sorted(array)
    return array[(len(array)-1)//2]