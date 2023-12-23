import sys
input = sys.stdin.readline

str = input().rstrip() # 백만
word = input().rstrip() # 36

stack = []
l = len(word)

for i in range(len(str)): 
    stack.append(str[i])
    if ''.join(stack[-l:]) == word:
        for _ in range(l):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))