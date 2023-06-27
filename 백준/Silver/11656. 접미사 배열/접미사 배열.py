string = input()
suffix = []
for i in range(len(string)):
    suffix.append(string[i:])
for x in sorted(suffix):
    print(x)