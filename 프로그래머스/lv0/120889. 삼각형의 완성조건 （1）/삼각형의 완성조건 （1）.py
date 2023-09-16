def solution(sides):
    sides = sorted(sides)

    return 2 if (sides[0]+sides[1])<=sides[2] else 1