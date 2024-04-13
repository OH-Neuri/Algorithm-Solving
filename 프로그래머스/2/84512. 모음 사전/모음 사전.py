from itertools import product
def solution(word):
    words = ['A','E','I','O','U']
    dic = []
    for i in range(1,6):
        dic.extend(list(product(words,repeat=i)))
    dic.sort()
    combined_dict = []
    
    for d in dic:
        combined_dict.append("".join(d))
    
    return combined_dict.index(word)+1