from math import sqrt

def solution(r1, r2):
    quar = 0
    for i in range(0, r1):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        quar += int(sqrt(r2**2 - i**2))
    return quar * 4