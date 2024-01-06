from collections import Counter
def solution(str1, str2):
    str1_arr = []
    str2_arr = []
    
    # 교집합 중복 허용
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            str1_arr.append(tmp.upper())
    
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            str2_arr.append(tmp.upper())
    
    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter)/len(union) * 65536)
