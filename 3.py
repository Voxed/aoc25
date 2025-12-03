import numpy as np
import re

b0 = [np.array(list(e.strip()), dtype=int) for e in open(0)]

def largest(b, nums):
    if nums == 0:
        return ''
    if -nums+1 != 0:
        first = np.argmax(b[:-nums+1])
    else:
        first = np.argmax(b)
    rest = b[first+1:]
    return str(b[first]) + largest(rest, nums - 1)

sum = 0
for bank in b0:
    sum += int(largest(bank, 12))