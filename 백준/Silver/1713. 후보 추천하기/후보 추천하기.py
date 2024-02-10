import sys


def find_key(dt, v):
    for key, value in dt.items():
        if value == v:
            return key


N = int(sys.stdin.readline())
rec_num = int(sys.stdin.readline())
li = map(int, sys.stdin.readline().split())

rec = list()
rec_cnt = dict()
for i in li:
    if len(rec) < N:
        if i not in rec:
            rec.append(i)
        rec_cnt[i] = rec_cnt.get(i, 0) + 1
    else:
        if i in rec:
            rec_cnt[i] = rec_cnt.get(i, 0) + 1
        else:
            m = find_key(rec_cnt, min(rec_cnt.values()))
            rec_cnt.pop(m)
            idx = rec.index(m)
            rec.pop(idx)

            rec.insert(idx, i)
            rec_cnt[i] = rec_cnt.get(i, 0) + 1

rec.sort()
for i in rec:
    print(i, end=" ")