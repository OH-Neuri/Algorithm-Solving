def solution(nums):
    answer=0
    sets = set(nums)
    if len(nums)/2<len(sets):
        answer= int((len(nums)/2))
    else:
        answer = (len(sets))
    return answer
