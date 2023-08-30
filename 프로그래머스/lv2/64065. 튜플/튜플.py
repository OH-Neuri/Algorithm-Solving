import re
def solution(s):
    answer = []
    li = re.findall('\d+(?:\,\d+)*',s)
    li = sorted(li,key=len)
    for i in li:
        for num in i.split(','):
            if int(num) not in answer:
                answer.append(int(num))

    return answer