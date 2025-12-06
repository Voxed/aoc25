import numpy as np
T = np.transpose
from itertools import groupby

def run(eqs):
    sum = 0
    for eq in eqs:
        match eq:
            case (n, '*'): sum += np.prod(n)
            case (n, '+'): sum += np.sum(n)
    return sum

lines = [l[:-1] for l in open(0)]
digits = len(lines)-1
ops = lines[-1].split()
raw_terms = lines[:-1]

# Parse and execute equations as specified in Part 1
terms = T([[*map(int, l.split())] for l in raw_terms])
print(run(zip(terms, ops)))

# Parse and execute equations as specified in Part 2
terms = [
    [*map(int, e)] for c, e in
    groupby(
        map(''.join, T([[*e] for e in raw_terms])),
        lambda s: s == ' '*digits)
    if not c
]
print(run(zip(terms, ops)))
