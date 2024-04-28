ppap_str = input()
stack = []
for p in ppap_str:
    stack.append(p)
    if len(stack)>=4:
        if stack[-4:] ==['P','P','A','P']:
            for _ in range(3):
                stack.pop()

if stack == ["P"]:
    print("PPAP")
else: print("NP")