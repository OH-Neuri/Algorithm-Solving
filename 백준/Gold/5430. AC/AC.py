def execute_funcion(fn, q):
    # False : left, True : right
    dir = False
    for f in fn:
        if f == "R":
            dir = not dir
        if f == "D":
            if len(q) < 1:
                return -1
            else:
                if not dir:
                    q.popleft()
                else:
                    q.pop()

    if not dir:
        return list(q)
    else:
        return list(q)[::-1]

from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    fn = list(input().rstrip())
    n = int(input())
    if n == 0:
        tmp_arr = input()
        arr = []
    else:
        arr = list(map(int,input().rstrip().replace("[","").replace("]","").split(",")))

    q = deque(arr)
    result = execute_funcion(fn,q)
    if result == -1:
        print("error")
    elif result == []:
        print([])
    else:
        result_str = ""
        for r in result:
            result_str += str(r) + ","
        print("["+result_str[:-1]+"]")

