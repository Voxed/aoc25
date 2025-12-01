import numpy as np
import itertools
#1
a = [int(l2[1:]) * (-1 if l2[0] == 'L' else 1) for l2 in [l.strip() for l in open("input.txt").readlines()]]
d = 50
s = 0
for l in a:
    d += l 
    d = d % 100
    if d == 0:
        s += 1
print(s)

#2
a = list(itertools.chain(*[[int(np.sign(l3))] * abs(l3) for l3 in a]))
d = 50
s = 0
for l in a:
    d += l 
    d = d % 100
    if d == 0:
        s += 1
print(s)

