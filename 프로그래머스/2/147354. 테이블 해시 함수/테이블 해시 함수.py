from collections import Counter

def solution(data, col, row_begin, row_end):
    sum_xor = 0
    data.sort(key=lambda x:(x[col-1],-x[0]))

    mod_counter = Counter()
    for i in range(row_begin-1, row_end):
        row_mod = 0
        for c in range(len(data[0])):
            row_mod += data[i][c] % (i+1)
        mod_counter[row_mod] += 1

    for mod_val, count in mod_counter.items():
        if count % 2 != 0:
            sum_xor ^= mod_val
    
    return sum_xor