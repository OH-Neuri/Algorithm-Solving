from collections import Counter
def solution(topping):
    answer = 0
    a = Counter(topping)
    b = {}
    for i in range(len(topping)):
        if topping[i] in a.keys():
            a[topping[i]] -=1
            if a[topping[i]] ==0:
                del a[topping[i]]
            if topping[i] in b.keys():
                b[topping[i]]+=1
            else:
                b[topping[i]]=1
        if len(a)==len(b):
            answer+=1
    return answer
