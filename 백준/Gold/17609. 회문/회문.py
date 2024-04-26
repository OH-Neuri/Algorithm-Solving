import sys
input = sys.stdin.readline

TC = int(input())
def is_palinderome(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] == word[right]:
            left +=1
            right -=1
        else:
            if right-left == 1:
                return 1
            if left < right -1:
                temp = word[:right] + word[right+1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left +1 < right:
                temp = word[:left] + word[left+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(TC):
    word = input().rstrip()
    print(is_palinderome(word))
